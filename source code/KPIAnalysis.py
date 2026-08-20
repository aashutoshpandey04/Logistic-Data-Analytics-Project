#Averagedeliverytime

avg_delivery_time = df['Delivery_Duration'].mean()

print(
    f"Average Delivery Time: "
    f"{avg_delivery_time:.2f} minutes"
)

#Ordersperride

orders_per_rider = (
    len(df) /
    df['Rider_ID'].nunique()
)

print(
    f"Orders per Rider: "
    f"{orders_per_rider:.2f}"
)

#Averagedistance

print(
    "Average Distance:",
    df['Distance_km'].mean()
)
