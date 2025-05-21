from src.data_loader import load_data, split_data
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import pickle
import os
import matplotlib.pyplot as plt

MODEL_DIR = "model"
os.makedirs(MODEL_DIR, exist_ok=True)

def train_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)

    models = {
        "RandomForest": RandomForestClassifier(),
        "XGBoost": XGBClassifier(eval_metric='logloss')
    }

    results = {}  # <-- zapisz wyniki obu modeli

    best_model = None
    best_score = 0

    for name, model in models.items():
        print(f"\n== Trenuję model: {name} ==")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = model.score(X_test, y_test)

        results[name] = score  # <-- zapisz dokładność

        print(classification_report(y_test, y_pred))

        if score > best_score:
            best_model = model
            best_score = score
            best_name = name

    # Wyznacz gorszy model
    worst_name = [n for n in results if n != best_name][0]
    worst_score = results[worst_name]

    print(f"\n✅ Najlepszy model: {best_name} (accuracy: {best_score:.2f})")
    print(f"❌ Gorszy model: {worst_name} (accuracy: {worst_score:.2f})")

    # Zapisz najlepszy model
    with open(os.path.join(MODEL_DIR, "malware_classifier.pkl"), "wb") as f:
        pickle.dump(best_model, f)
    print(f"Model zapisany jako: {MODEL_DIR}/malware_classifier.pkl")

    # Pokaż ważność cech
    importances = best_model.feature_importances_
    features = X.columns

    plt.figure(figsize=(10, 6))
    plt.barh(features, importances)
    plt.title(f"Ważność cech ({best_name})")
    plt.xlabel("Wartość")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.barh(features, importances)
    plt.title(f"Ważność cech ({worst_name})")
    plt.xlabel("Wartość")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    train_model()
