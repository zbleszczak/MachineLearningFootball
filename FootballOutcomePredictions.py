import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import *

# Load the data
from sklearn.preprocessing import LabelEncoder

data = pd.read_excel("premierleagueall.xlsx")

# Create a LabelEncoder object
le = LabelEncoder()

# Encode the team names
data["HomeTeam"] = le.fit_transform(data["HomeTeam"])
data["AwayTeam"] = le.fit_transform(data["AwayTeam"])

# Define the features
features = ["HomeTeam", "AwayTeam", "HS", "AS", "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR"]

# Index the data DataFrame using column names
X = data.loc[:, features]

# Train the model
y = data["FTR"].values
model = LinearRegression()
model.fit(X, y)

# Make predictions
team_a = 1
team_b = 2
prediction = model.predict([[team_a, team_b]])

# Print the prediction
print(prediction)
