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

