import argparse
from src import train
from src import predict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Malware Classifier CLI")
    parser.add_argument('--train', action='store_true', help='Wytrenuj model')
    parser.add_argument('--predict', type=str, help='Ścieżka do pliku CSV z cechami do klasyfikacji')

    args = parser.parse_args()

    if args.train:
        train.train_model()
    elif args.predict:
        predict.predict(args.predict)
    else:
        print("Użycie:\n --train (do treningu) lub --predict <plik.csv>")
