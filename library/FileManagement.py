import os
import json
import pickle

folder = "data_gwehjj"

if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Folder {folder} created.")

else:
    print(f"Folder {folder} already exists.")

nama = input("Masukkan nama user: ")
email = input("Masukkan email user: ")
umur = input("Masukkan umur user: ")

data_user = {
    "nama": nama,
    "email": email,
    "umur": umur
}

"""
filepath_json = os.path.join(folder, "user_data.json")
filepath_pickle = os.path.join(folder, "user_data.pkl")

"""
filepath_json = os.path.join(folder, f"{nama.lower()}.json")
filepath_pickle = os.path.join(folder, f"{nama.lower()}.pkl")

with open(filepath_json, 'w') as json_file:
    json.dump(data_user, json_file)
    print(f"Data user disimpan dalam format JSON di {filepath_json}.")

with open(filepath_pickle, 'wb') as pickle_file:
    pickle.dump(data_user, pickle_file)
    print(f"Data user disimpan dalam format Pickle di {filepath_pickle}.")

with open(filepath_json, 'r') as json_file:
    data_loaded_json = json.load(json_file)
    print("Data yang dimuat dari file JSON:")
    print(data_loaded_json)
