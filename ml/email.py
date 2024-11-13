import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv('emails.csv')

data.head()

data.info()

data.isnull().sum()

# Combine relevant columns into a single text column

data['email_content'] = (
    data['the'].astype(str) + ' ' +
    data['to'].astype(str) + ' ' +
    data['ect'].astype(str) + ' ' +
    data['and'].astype(str) + ' ' +
    data['military'].astype(str) + ' ' +
    data['allowing'].astype(str) + ' ' +
    data['ff'].astype(str) + ' ' +
    data['dry'].astype(str)
)

# Define features and target
X = data['email_content']
y = data['Prediction']

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split into train & test data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size = 0.2, random_state=42)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

print('KNN Classification report:\n', classification_report(y_test, y_pred_knn))
print('KNN Confusion matrix:\n', confusion_matrix(y_test, y_pred_knn))

# SVM
svm = SVC()
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

print('SVM Classification report:\n', classification_report(y_test, y_pred_svm))
print('SVM Confusion matrix:\n', confusion_matrix(y_test, y_pred_svm))
