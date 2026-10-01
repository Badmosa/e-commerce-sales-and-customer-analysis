# E-Commerce Sales & Customer Analytics

This is an exploratory data analysis (EDA) of 138,000+ e-commerce orders, built with Python and pandas. The notebook digs into sales performance, profitability, customer behavior, marketing effectiveness, delivery/logistics, and returns.

## 📊 Dataset

- Source: E-Commerce Sales and Customer Analytics on `Kaggle` (downloaded automatically via kagglehub)
- Size: ~138,000 orders, 46 columns
- hat it covers: order details, customer demographics and segments, payment and shipping info, delivery performance, returns, marketing channels/campaigns, and profit metrics.

Columns include `order_id`, `order_date`, `sales_channel`, `customer_segment`, `customer_lifetime_value`, `net_sales`, `profit`, `profit_margin_percentage`, `delivery_days`, `return_status`, `marketing_channel`, `coupon_code`, and `payment_method`, among others.

## 🎯 What the notebook answers

The analysis is organized into six sections:

**1. Sales & Revenue**
- Revenue and order volume by sales channel
- Revenue by region
- Net sales trend over time (monthly)

2. **Profitability**

- Most profitable regions and channels (not just highest revenue)
- Whether discounts/coupons hurt profit margin
- Where costs are concentrated (product cost vs. shipping vs. tax vs. discounts)

3. **Customer Behavior & Segmentation**

- Highest-value customers by lifetime value
- Returning vs. new customer rate and spend comparison
- Spending patterns by customer segment/type
Buying patterns by age bracket and gender

4. **Marketing Effectiveness**

- Sales and order volume by marketing channel and campaign
- Coupon usage vs. order value and profit margin

5. **Logistics & Delivery Performance**

- Rate of delivery SLA breaches (actual vs. estimated delivery time), broken down by warehouse and shipping method

6. **Returns & Customer Satisfaction**

- Most common return reasons
- Whether review sentiment correlates with returns
- Return rate by sales channel

**Payment Behavior**

- Payment status (success/pending/failed) breakdown by payment method

**🛠️ Tools & Libraries**
- Python 3
- pandas
- kagglehub (for downloading the dataset directly from Kaggle)

📁 **Repo structure**
- ├── e-commerce-sales-and-customer-analytics.ipyn  # Main analysis notebook
- ├── import kagglehub.py                               # Standalone script to fetch/preview the dataset
- └── README.md

**Run Cell:**

jupyter notebook e-commerce-sales-and-customer-analytics.ipynb

### 📌 Notes
- This notebook focuses on data manipulation and business-question answering with pandas rather than charting — every result is a table/aggregation, so it doubles well as a pandas practice reference (groupby, agg, resample, pd.cut, correlation, etc.).

- Some fields are naturally sparse by design (e.g., return_reason and coupon_code are only populated when applicable), which is reflected in the "Data Inspection" section.

