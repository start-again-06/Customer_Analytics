import pandas as pd

def load_data(file_path):
    """Load customer data from a CSV file."""
    return pd.read_csv(file_path)

def calculate_clv(df):
    """Calculate Customer Lifetime Value (CLV)."""
    df['TotalRevenue'] = df['AverageOrderValue'] * df['PurchaseFrequency']
    df['CLV'] = df['TotalRevenue'] * df['CustomerLifespan']
    return df[['CustomerID', 'CLV']]

def retention_rate(df):
    """Calculate customer retention rate."""
    total_customers = df['CustomerID'].nunique()
    retained_customers = df[df['IsRetained'] == 1]['CustomerID'].nunique()
    return retained_customers / total_customers

def churn_rate(df):
    """Calculate customer churn rate."""
    return 1 - retention_rate(df)

def main():
    file_path = "customer_data.csv"  # Replace with actual file path
    df = load_data(file_path)
    
    clv_df = calculate_clv(df)
    print("Customer Lifetime Value (CLV):\n", clv_df.head())
    
    print("Retention Rate:", retention_rate(df))
    print("Churn Rate:", churn_rate(df))

if __name__ == "__main__":
    main()
