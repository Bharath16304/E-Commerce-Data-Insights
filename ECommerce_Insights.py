import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('ecommerce_data.csv')  # columns: product, user_id, order_quantity, review_score

# Top-Selling Products
top_products = df.groupby('product')['order_quantity'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar', title='Top Selling Products')
plt.show()

# Peak Hours (Assuming 'order_time' column exists)
df['order_time'] = pd.to_datetime(df['order_time'])
df['hour'] = df['order_time'].dt.hour
df['hour'].value_counts().sort_index().plot(kind='line', title='Orders by Hour')
plt.show()

# User Retention (Assuming 'user_id' and 'order_date')
df['order_date'] = pd.to_datetime(df['order_date'])
retention = df.groupby('user_id')['order_date'].nunique()
retention.hist(bins=20)
plt.title('User Retention Distribution')
plt.xlabel('Number of Active Days')
plt.show()
