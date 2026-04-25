# Convert date
df['Dates'] = pd.to_datetime(df['Dates'])
df = df.sort_values('Dates')

# Plot
plt.figure(figsize=(10,5))
plt.plot(df['Dates'], df['Prices'], marker='o')
plt.title("Natural Gas Prices")
plt.show()


# Convert dates to numeric
df['Days'] = (df['Dates'] - df['Dates'].min()).dt.days

# Create interpolation model
from scipy.interpolate import interp1d
model = interp1d(df['Days'], df['Prices'], kind='cubic', fill_value="extrapolate")

# Function to estimate price
def estimate_price(date):
    date = pd.to_datetime(date)
    days = (date - df['Dates'].min()).days
    return float(model(days))

# Test
print("Price on 2023-06-15:", estimate_price("2023-06-15"))
print("Price on 2025-05-01:", estimate_price("2025-05-01"))



# Future 1 year prediction
future_dates = pd.date_range(start=df['Dates'].max(), periods=12, freq='M')
future_prices = [estimate_price(d) for d in future_dates]

print("\nFuture Prices:")
for d, p in zip(future_dates, future_prices):
    print(d.date(), ":", round(p,2))



