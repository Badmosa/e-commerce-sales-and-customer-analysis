import kagglehub
import pandas as pd

path = kagglehub.dataset_download(
    "datascikhan/e-commerce-sales-and-customer-analytics"
)

file_path = path + "/ecommerce_sales_customer_analytics_150k.csv"

df = pd.read_csv(file_path)

df.head()

print(df.shape)
print(df.columns)
print(df.info())