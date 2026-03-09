import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

current_dir = os.path.dirname(__file__)
dataset_path = os.path.join(current_dir, "..", "Dataset", "cleaned_data.csv")

# 1. Load dataset
df = pd.read_csv(dataset_path)

print("Dataset size:", df.shape)
print(df.head())


# 2. Define inputs and labels
X = df["text"]
y = df["label"]


# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# 4. Text Vectorization
vectorizer = TfidfVectorizer(stop_words="english")

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


# 5. Train Model
model = LogisticRegression(max_iter=1000)

model.fit(X_train_vec, y_train)


# 6. Predictions
predictions = model.predict(X_test_vec)


# 7. Evaluation
print("\nModel Accuracy:")
print(accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))


# 8. Save Model
pickle.dump(model, open("../models/stress_model.pkl", "wb"))
pickle.dump(vectorizer, open("../models/vectorizer.pkl", "wb"))

print("\nModel and vectorizer saved successfully.")