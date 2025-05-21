import pickle
import pandas as pd

def load_model(path='model/malware_classifier.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)

def predict(file_path):
    model = load_model()
    df = pd.read_csv(file_path)
    predictions = model.predict(df)
    for i, pred in enumerate(predictions):
        label = "Złośliwy" if pred == 1 else "Bezpieczny"
        print(f"Plik {i+1}: {label}")
