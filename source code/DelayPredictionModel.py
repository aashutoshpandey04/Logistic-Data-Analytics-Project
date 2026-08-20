#Create Target Variable:

df['Delayed'] = (
    df['Delivery_Duration'] > 45
).astype(int)

#Encode Categories:

encoder = LabelEncoder()

df['Traffic'] = encoder.fit_transform(
    df['Traffic']
)

df['Weather'] = encoder.fit_transform(
    df['Weather']
)

#Select Features:

X = df[
    [
        'Distance_km',
        'Traffic',
        'Weather'
    ]
]

y = df['Delayed']

#Train Model
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(
    X_train,
    y_train
)

accuracy = model.score(
    X_test,
    y_test
)

print(
    f"Accuracy: "
    f"{accuracy*100:.2f}%"
)
