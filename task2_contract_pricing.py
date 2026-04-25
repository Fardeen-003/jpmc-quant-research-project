import pandas as pd
from scipy.interpolate import interp1d

# Load data
df = pd.read_csv("Nat_Gas.csv")
df['Dates'] = pd.to_datetime(df['Dates'])
df = df.sort_values('Dates')

# Convert dates to numeric
df['Days'] = (df['Dates'] - df['Dates'].min()).dt.days

# Create price model
price_model = interp1d(df['Days'], df['Prices'], kind='cubic', fill_value="extrapolate")

# Function to get price for any date
def get_price(date):
    date = pd.to_datetime(date)
    days = (date - df['Dates'].min()).days
    return float(price_model(days))

# 🚀 MAIN FUNCTION: Contract Pricing
def price_contract(injection_dates, withdrawal_dates, volume,
                   storage_cost_per_month, injection_cost, withdrawal_cost):

    total_value = 0

    for inj_date, wth_date in zip(injection_dates, withdrawal_dates):

        buy_price = get_price(inj_date)
        sell_price = get_price(wth_date)

        # Profit
        profit = (sell_price - buy_price) * volume

        # Storage duration (in months approx)
        inj_date = pd.to_datetime(inj_date)
        wth_date = pd.to_datetime(wth_date)
        months = (wth_date - inj_date).days / 30

        storage_cost = months * storage_cost_per_month

        # Total costs
        total_cost = storage_cost + injection_cost + withdrawal_cost

        # Net value
        total_value += (profit - total_cost)

    return total_value


# ✅ TEST EXAMPLE
injection_dates = ["2023-05-01"]
withdrawal_dates = ["2023-12-01"]

value = price_contract(
    injection_dates,
    withdrawal_dates,
    volume=1000000,  # 1 million units
    storage_cost_per_month=100000,
    injection_cost=10000,
    withdrawal_cost=10000
)

print("Contract Value:", round(value, 2))
