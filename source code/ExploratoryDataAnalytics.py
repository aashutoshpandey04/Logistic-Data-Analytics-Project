#Delivery Time Distribution

plt.figure(figsize=(8,5))

sns.histplot(
    df['Delivery_Duration'],
    bins=30
)

plt.title("Delivery Time Distribution")
plt.show()

#Distance vs Delivery Time

plt.figure(figsize=(8,5))

sns.scatterplot(
    x='Distance_km',
    y='Delivery_Duration',
    data=df
)

plt.title(
    "Distance vs Delivery Time"
)

plt.show()

#Traffic Condition Analysis

sns.boxplot(
    x='Traffic',
    y='Delivery_Duration',
    data=df
)

plt.show()
