import joblib

def load_model(path='models/aero_model.pkl'):
    return joblib.load(path)

def predict_adjustment(model, input_features):
    return model.predict([input_features])[0]
