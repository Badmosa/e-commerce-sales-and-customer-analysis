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

Most profitable regions and channels (not just highest revenue)
- Whether discounts/coupons hurt profit margin
- Where costs are concentrated (product cost vs. shipping vs. tax vs. discounts)