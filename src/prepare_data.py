import os
import csv
from extract_features import extract_features_from_exe

MALWARE_DIR = 'data/malware'
BENIGN_DIR = 'data/benign'
OUTPUT_FILE = 'data/simple_features.csv'

def extract_all_from_folder(folder, label):
    rows = []
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isfile(path) and (f.endswith('.exe') or f.endswith('.dll')):
            features = extract_features_from_exe(path)
            if features:
                rows.append(features + [label])
    return rows

malware_rows = extract_all_from_folder(MALWARE_DIR, 1)
benign_rows = extract_all_from_folder(BENIGN_DIR, 0)

with open(OUTPUT_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'entropy', 'num_sections', 'size', 'machine', 'time_date_stamp',
        'num_symbols', 'characteristics', 'subsystem', 'dll_characteristics',
        'size_of_image', 'size_of_headers', 'checksum', 'num_imports', 'label'
    ])
    writer.writerows(malware_rows + benign_rows)

print(f'Dane zapisane do {OUTPUT_FILE}')
