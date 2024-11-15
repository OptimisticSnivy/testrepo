import pandas as pd
import numpy as np

df = pd.read_csv("uber.csv")
df.info()
df.describe()
df.isnull().sum()

df["dropoff_latitude"] = df["dropoff_latitude"].fillna(df["dropoff_latitude"].mean())
df["dropoff_longitude"] = df["dropoff_longitude"].fillna(df["dropoff_longitude"].median())

df.isnull().sum()

import numpy as np

def remove_outliers(df, columns):
    # Looping through each specified column
    for col in columns:
        feature = df[col]
        q1 = feature.quantile(0.25)
        q3 = feature.quantile(0.75)
        IQR = q3 - q1
        lower_bound = float(q1 - 1.5 * IQR)  # Cast to float for precision
        upper_bound = float(q3 + 1.5 * IQR)  # Cast to float for precision

        # Replacing outliers with bounds
        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])

    return df

# Example usage: Remove outliers from 'fare_amount' column
df = remove_outliers(df, ['fare_amount'])

df=df.drop(['Unnamed: 0','key'],axis=1)

# Checking outliers by plot
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 4))
plt.boxplot(df["fare_amount"])
plt.xlabel("Fare Amount")
plt.ylabel("Fare")
plt.title("Box-Plot check for outliers")
plt.show()

# Removal of unreqd. & date std.

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], utc=True)
df["year"] = df["pickup_datetime"].dt.year
df["month"] = df["pickup_datetime"].dt.month
df["day"] = df["pickup_datetime"].dt.day
df["hour"] = df["pickup_datetime"].dt.hour
df["minute"] = df["pickup_datetime"].dt.minute
df["second"] = df["pickup_datetime"].dt.second
df["weekday"] = df["pickup_datetime"].dt.weekday
df.drop(["pickup_datetime"], axis=1)
df.head()

# correlation
import seaborn as sns
import matplotlib.pyplot as plt

# Select only numeric columns for the correlation matrix
numeric_df = df.select_dtypes(include=[np.number])

# Calculate the correlation matrix
corr = numeric_df.corr()

# Plot the heatmap
plt.figure(figsize=(15, 8))
sns.heatmap(corr, annot=True)
plt.show()


# Distance calculation
import math

def haversine_formula(lat1, lon1, lat2, lon2):
    # Conversion to rad
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Havrsine formula
    dion = lon2 - lon1
    diat = lat2 - lat1
    a = math.sin(diat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dion/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Radius of earth in km is 6371
    km = 6371 * c
    return km

# Running models

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Calculate and make a feature

df['distance_km'] = df.apply(lambda row: haversine_formula(row['pickup_latitude'], row['pickup_longitude'],row['dropoff_latitude'],row['dropoff_longitude']), axis=1 )

# Define features and target
X = df[['distance_km']]
y = df['fare_amount']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
linear_reg = LinearRegression()
rf_reg = RandomForestRegressor()

# Fit models
linear_reg.fit(X_train, y_train)
rf_reg.fit(X_train, y_train)

# Predict on test set
y_pred_lr = linear_reg.predict(X_test)
y_pred_rf = rf_reg.predict(X_test)

# Evaluate models
r2_lr = r2_score(y_test, y_pred_lr)
rmse_lr = mean_squared_error(y_test, y_pred_lr, squared=False)

r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = mean_squared_error(y_test, y_pred_rf, squared=False)

# Print evaluation metrics
print(f"Linear Regression R2: {r2_lr:.4f}, RMSE: {rmse_lr:.4f}")
print(f"Random Forest Regression R2: {r2_rf:.4f}, RMSE: {rmse_rf:.4f}")
