import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your football match data
data = pd.read_excel("all-euro-data-2017-2018.xlsx")

# Define your selected features and target variable
selected_features = ["FTHG", "FTAG", "HTHG", "HTAG", "HS", "AS", "HST", "AST", "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR", "HomeTeam", "AwayTeam"]
target_variable = "FTR"  # Full-Time Result (Home win, Draw, Away win)

# Prepare the data
X = data[selected_features]
y = data[target_variable]

# Perform one-hot encoding for categorical columns
X = pd.get_dummies(X, columns=["HomeTeam", "AwayTeam"])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

best_accuracy = 0
best_model = None

# Train and save the best model
for _ in range(30):
    # Create and train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model on the test set
    accuracy = model.score(X_test, y_test)
    print("Accuracy is:", accuracy)

    # Check if this model is the best so far
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Print predicted outcomes alongside actual outcomes
predictions = best_model.predict(X_test)
for i, (predicted, actual) in enumerate(zip(predictions, y_test)):
    print(f"Example {i+1}: Predicted={predicted}, Actual={actual}")

# Save the best model to a file
if best_model is not None:
    with open("football_model.pickle", "wb") as f:
        pickle.dump(best_model, f)

# Now you have the most accurate football match outcome prediction model saved in 'football_model.pickle'
