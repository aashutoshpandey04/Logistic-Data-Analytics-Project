# Missing values
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(method='ffill', inplace=True)

print("Data cleaned successfully")
