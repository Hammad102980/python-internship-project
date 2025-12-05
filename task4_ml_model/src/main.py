import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

print("🚀 === Task 4: ML Spam Classifier STARTING ===")

class SpamClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
        self.model = MultinomialNB()
    
    def load_data(self):
        data = {
            'text': [
                'win free money now click here', 'urgent loan approval call now', 'buy cheap viagra online',
                'meeting tomorrow 10am office', 'hello how are you today', 'please review attached document',
                'claim your free prize today', 'double your money guaranteed', 'lunch at 1pm conference room',
                'congratulations you won 1 million dollars', 'free gift card waiting for you',
                'team meeting scheduled for monday', 'update your account information now',
                'happy birthday celebration party', 'project deadline extended to friday'
            ],
            'label': ['spam', 'spam', 'spam', 'ham', 'ham', 'ham', 'spam', 'spam', 'ham', 
                     'spam', 'spam', 'ham', 'spam', 'ham', 'ham']
        }
        df = pd.DataFrame(data)
        print("📊 Dataset: Spam/Ham emails")
        print(df['label'].value_counts())
        return df
    
    def train_and_evaluate(self):
        df = self.load_data()
        X = df['text']
        y = df['label']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)
        
        self.model.fit(X_train_vec, y_train)
        y_pred = self.model.predict(X_test_vec)
        
        accuracy = accuracy_score(y_test, y_pred)
        print(f"\n🎯 MODEL ACCURACY: {accuracy:.2%}")
        print("\n📈 Classification Report:")
        print(classification_report(y_test, y_pred))
        
        # Save model
        Path(__file__).resolve().parent.parent.joinpath('models').mkdir(exist_ok=True)
        joblib.dump(self.vectorizer, '../models/vectorizer.pkl')
        joblib.dump(self.model, '../models/spam_classifier.pkl')
        print("💾 Model saved: models/spam_classifier.pkl")
        
        return accuracy

def test_model():
    print("\n🧪 Testing new emails:")
    classifier = SpamClassifier()
    classifier.model = joblib.load('../models/spam_classifier.pkl')
    classifier.vectorizer = joblib.load('../models/vectorizer.pkl')
    
    test_emails = [
        "Win FREE iPhone 15! Click now!",
        "Team meeting tomorrow 10 AM office"
    ]
    
    for email in test_emails:
        vec = classifier.vectorizer.transform([email])
        pred = classifier.model.predict(vec)[0]
        prob = max(classifier.model.predict_proba(vec)[0])
        print(f"'{email[:40]}...' → {pred} ({prob:.2%} confidence)")

def main():
    print("📦 Creating model directories...")
    Path('../models').mkdir(exist_ok=True)
    Path('../data').mkdir(exist_ok=True)
    
    classifier = SpamClassifier()
    accuracy = classifier.train_and_evaluate()
    
    print(f"\n🎉 TASK 4 SUCCESS! Accuracy: {accuracy:.2%}")
    print("✅ Files created:")
    print("   models/spam_classifier.pkl")
    print("   models/vectorizer.pkl")
    
    test_model()
    print("\n🏆 ALL 4 INTERNSHIP TASKS COMPLETED! 🚀")

if __name__ == "__main__":
    main()
