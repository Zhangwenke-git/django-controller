import os
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent

if __name__ =="__main__":
    reports = os.path.join(BASE_DIR, r'templates\ant')
    for root, dirs, files in os.walk(reports):
        for file in files:
            if file.endswith(".html") or file.endswith(".xml"):
                delete_file = os.path.join(root, file)
                os.remove(delete_file)
