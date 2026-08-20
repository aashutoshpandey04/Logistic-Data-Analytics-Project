df['Order_Date'] = pd.to_datetime(df['Order_Date'])

df['Pickup_Time'] = pd.to_datetime(df['Pickup_Time'])

df['Delivery_Time'] = pd.to_datetime(df['Delivery_Time'])
