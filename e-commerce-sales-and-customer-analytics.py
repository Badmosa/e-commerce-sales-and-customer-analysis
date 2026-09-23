import kagglehub
import pandas as pd

path = kagglehub.dataset_download(
    "datascikhan/e-commerce-sales-and-customer-analytics"
)

file_path = path + "/ecommerce_sales_customer_analytics_150k.csv"

df = pd.read_csv(file_path)

df.head()

# # Data Inspection
# print(df.columns)


# # Inspecting the dataset info.
# print(df.info())

# # Inspecting for duplicates in the dataset.
# df.duplicated().sum()
 

# 1. SALES & REVENUE
 
def sales_by_channel(df):
    """Revenue and order volume by sales channel."""
    return (
        df.groupby("sales_channel")
        .agg(orders=("order_id", "count"),
             gross_sales=("gross_sales", "sum"),
             net_sales=("net_sales", "sum"))
        .sort_values("net_sales", ascending=False)
    )
 
 
def sales_by_region(df):
    """Revenue by region."""
    return (
        df.groupby("region")
        .agg(orders=("order_id", "count"), net_sales=("net_sales", "sum"))
        .sort_values("net_sales", ascending=False)
    )
 
 
def revenue_over_time(df, freq="M"):
    """Net sales trend over time. freq: 'D' daily, 'W' weekly, 'M' monthly."""
    d = df.copy()
    d["order_date"] = pd.to_datetime(d["order_date"])
    return d.set_index("order_date").resample(freq)["net_sales"].sum()
 
 
def gross_vs_net_gap(df):
    """How much revenue is lost to discounts, tax, and shipping."""
    total_gross = df["gross_sales"].sum()
    total_discount = df["discount_amount"].sum()
    total_tax = df["tax_amount"].sum()
    total_shipping = df["shipping_cost"].sum()
    total_net = df["net_sales"].sum()
    return pd.Series({
        "gross_sales": total_gross,
        "discount_amount": total_discount,
        "tax_amount": total_tax,
        "shipping_cost": total_shipping,
        "net_sales": total_net,
        "gap_pct": round((total_gross - total_net) / total_gross * 100, 2)
    })
