import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pickle
import pandas as pd
from src.data_loader import load_data, split_data
from src.train import train_model
from src.predict import load_model

class TestMalwareClassifier(unittest.TestCase):

    def test_data_loading(self):
        X, y = load_data()
        self.assertEqual(len(X), len(y))
        self.assertGreater(len(X), 0)

    def test_model_training(self):
        train_model()
        self.assertTrue(os.path.exists('model/malware_classifier.pkl'))

    def test_model_prediction_shape(self):
        model = load_model()
        X, _ = load_data()
        y_pred = model.predict(X[:5])
        self.assertEqual(len(y_pred), 5)

    def test_model_prediction_labels(self):
        model = load_model()
        X, _ = load_data()
        preds = model.predict(X[:5])
        for p in preds:
            self.assertIn(p, [0, 1])

if __name__ == '__main__':
    unittest.main()
