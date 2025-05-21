import pefile
import os
import math

def calculate_entropy(data):
    if not data:
        return 0.0
    entropy = 0
    for x in range(256):
        p_x = data.count(bytes([x])) / len(data)
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)
    return entropy

import pefile
import os
import math

def calculate_entropy(data):
    if not data:
        return 0.0
    entropy = 0
    for x in range(256):
        p_x = data.count(bytes([x])) / len(data)
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)
    return entropy

def extract_features_from_exe(file_path):
    try:
        pe = pefile.PE(file_path)
        entropy = calculate_entropy(open(file_path, 'rb').read())
        num_sections = len(pe.sections)
        size = os.path.getsize(file_path)

        # Każda cecha z osobnym zabezpieczeniem:
        try: machine = pe.FILE_HEADER.Machine
        except: machine = 0

        try: time_date_stamp = pe.FILE_HEADER.TimeDateStamp
        except: time_date_stamp = 0

        try: num_symbols = pe.FILE_HEADER.NumberOfSymbols
        except: num_symbols = 0

        try: characteristics = pe.FILE_HEADER.Characteristics
        except: characteristics = 0

        try:
            optional_header = pe.OPTIONAL_HEADER
            subsystem = optional_header.Subsystem
            dll_characteristics = optional_header.DllCharacteristics
            size_of_image = optional_header.SizeOfImage
            size_of_headers = optional_header.SizeOfHeaders
            checksum = optional_header.CheckSum
        except:
            subsystem = dll_characteristics = size_of_image = size_of_headers = checksum = 0

        try: num_imports = len(pe.DIRECTORY_ENTRY_IMPORT)
        except: num_imports = 0

        return [
            entropy,
            num_sections,
            size,
            machine,
            time_date_stamp,
            num_symbols,
            characteristics,
            subsystem,
            dll_characteristics,
            size_of_image,
            size_of_headers,
            checksum,
            num_imports
        ]

    except Exception as e:
        print(f"Błąd ekstrakcji cech z {file_path}: {e}")
        return None

