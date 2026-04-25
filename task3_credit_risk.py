import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset (update filename if needed)
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Check data
print(df.head())

# Features (example — adjust based on your dataset)
X = df.drop(columns=["default"])   # target column = default (0 or 1)
y = df["default"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))



# Function to calculate expected loss

def calculate_expected_loss(input_data, loan_amount):
    """
    input_data: list of borrower features (same order as training data)
    loan_amount: total loan
    """

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data], columns=X.columns)

    # Predict probability of default
    pd_value = model.predict_proba(input_df)[0][1]

    # Expected loss formula
    recovery_rate = 0.1
    expected_loss = pd_value * (1 - recovery_rate) * loan_amount

    return pd_value, expected_loss





# Example input (change based on your dataset columns)
sample_input = X.iloc[0].values.tolist()

pd_value, loss = calculate_expected_loss(sample_input, loan_amount=500000)

print("Probability of Default:", round(pd_value, 4))
print("Expected Loss:", round(loss, 2))
