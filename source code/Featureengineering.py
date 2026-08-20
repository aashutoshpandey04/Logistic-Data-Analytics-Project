#Delivery Duration

df['Delivery_Duration'] = (
    df['Delivery_Time']
    - df['Pickup_Time']
).dt.total_seconds()/60

#Hour of day

df['Order_Hour'] = df['Order_Date'].dt.hour
