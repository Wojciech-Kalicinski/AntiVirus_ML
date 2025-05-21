import pickle

def save_model(model, path='model/malware_classifier.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_model(path='model/malware_classifier.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)
