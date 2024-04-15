import pandas as pd
file_path = "C:\Users\bvyb0\Downloads\archive\TruMedicines-Pharmaceutical-images20k.dataset"
# above .data file is comma delimited
wine_data = pd.read_csv(file_path, delimiter=",")