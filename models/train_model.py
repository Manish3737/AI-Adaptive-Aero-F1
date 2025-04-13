import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Load preprocessed data
    df = pd.read_pickle('data/preprocessed_data.pkl')
    
    # Features and dummy labels (for example purposes)
    X = df[['normalized_speed', 'is_cornering', 'normalized_temp', 'proximity_score']]
    y = [1, 0, 1, 0, 1]  # Dummy targets: 1 = high downforce, 0 = low downforce

    model = RandomForestClassifier()
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'models/aero_model.pkl')
    print("✅ Model trained and saved as aero_model.pkl")

if __name__ == "__main__":
    train_model()
