# 🛡️ Malware Classifier – EXE/DLL File Classifier

This project enables automatic detection of malicious software based on technical features extracted from `.exe` and `.dll` files. By analyzing PE headers and file entropy, you can train a machine learning model to classify files as **malicious** or **benign**.

---

## 📁 Folder and File Structure

├── data/
│ ├── benign/ ← place safe .exe/.dll files here
│ ├── malware/ ← place malicious .exe/.dll files here
├── extract_features.py ← extracts features from EXE/DLL files
├── prepare_data.py ← generates a CSV file with features for all files
├── prepare_utils.py ← functions for loading and splitting data
├── main.py ← trains and tests the classification model
├── data/simple_features.csv ← generated dataset file

 

---

## ✅ Step-by-Step Guide

### 1. Prepare your data

Create the folder structure `data/benign` and `data/malware`, then:

- Add **benign** `.exe` or `.dll` files to `data/benign/`
- Add **malicious** `.exe` or `.dll` files to `data/malware/`

> You can use samples from VirusTotal, MalwareBazaar, or your own files.

---

### 2. Generate the dataset

Run the following script in your terminal:

```bash
python prepare_data.py
This script:

Calls extract_features_from_exe() for each file,

Collects features into a list,

Creates the data/simple_features.csv file with labels: 0 (benign), 1 (malicious).

3. Train the model and view results
Run the following script:

 
python main.py
This script:

Loads the CSV dataset,

Splits data into training and testing sets (50/50),

Trains a RandomForest classifier,

Displays the accuracy and classification report.

📄 File Descriptions
extract_features.py
Contains the extract_features_from_exe(file_path) function, which:

Parses EXE/DLL files using pefile,

Extracts features such as entropy, number of sections, file size, imports, etc.,

Returns 13 numeric features describing the file.

prepare_data.py
Loads files from data/benign/ and data/malware/,

Extracts features using extract_features_from_exe,

Saves the result to data/simple_features.csv for ML usage.

prepare_utils.py
load_data() – loads the dataset and splits it into X (features) and y (labels),

split_data() – splits data into training/testing sets with stratified labels.

main.py
Uses prepare_utils.py to:

Load and split the dataset,

Train a RandomForestClassifier,

Display the performance using classification_report.

📊 Features Used for Classification
Each executable file is analyzed for the following features:

entropy – byte entropy (randomness measure)

num_sections – number of sections in the file

size – file size in bytes

machine, time_date_stamp, num_symbols, characteristics

subsystem, dll_characteristics, size_of_image, size_of_headers, checksum

num_imports – number of imported libraries

📦 Requirements
Make sure Python 3 is installed and run:

 
pip install pandas scikit-learn pefile
⚠️ Disclaimer
This project is intended for educational purposes only. It is not a replacement for professional antivirus tools and does not guarantee 100% accuracy.
Do not run suspicious files on your machine.