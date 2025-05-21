import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path='data/simple_features.csv'):
    df = pd.read_csv(path)

    X = df[
        ['entropy', 'num_sections', 'size', 'machine', 'time_date_stamp',
         'num_symbols', 'characteristics', 'subsystem', 'dll_characteristics',
         'size_of_image', 'size_of_headers', 'checksum', 'num_imports']
    ]
    y = df['label']

    return X, y

def split_data(X, y, test_size=0.5, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
