import pandas as pd

# Load dataset
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Check data
print(df.head())



num_buckets = 5

df['fico_bucket'] = pd.qcut(df['fico_score'], q=num_buckets, labels=False)



df['rating'] = num_buckets - df['fico_bucket']


bucket_summary = df.groupby('rating').agg(
    total=('default', 'count'),
    defaults=('default', 'sum')
)

bucket_summary['pd'] = bucket_summary['defaults'] / bucket_summary['total']

print(bucket_summary)




def get_rating(fico_score, df, num_buckets=5):
    # Recreate bins
    bins = pd.qcut(df['fico_score'], q=num_buckets, retbins=True, duplicates='drop')[1]
    
    for i in range(len(bins)-1):
        if bins[i] <= fico_score <= bins[i+1]:
            return num_buckets - i




print("Rating for FICO 720:", get_rating(720, df))
