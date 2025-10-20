import os
import pickle

# Nama folder tempat data disimpan
folder = "data_gwehjj"

print("--- Data Pengguna Terdaftar ---")

# Cek dulu apakah foldernya ada
if os.path.exists(folder):
    # os.listdir() akan memberikan list semua nama file di dalam folder
    for nama_file in os.listdir(folder):
        # Kita hanya mau memproses file yang berakhiran .pkl
        if nama_file.endswith(".pkl"):
            # Gabungkan path folder dan nama file
            path_lengkap = os.path.join(folder, nama_file)

            # Buka dan baca file pickle
            with open(path_lengkap, 'rb') as file:
                try:
                    # 'pickle.load()' untuk kembalikan objek dari file pickle
                    data = pickle.load(file)
                    print(
                        f"Nama: {
                            data['nama']},Email: {
                            data['email']}, Umur: {
                            data['umur']}")
                except Exception as e:
                    print(f"Gagal membaca file {nama_file}: {e}")
else:
    print(f"Folder '{folder}' tidak ditemukan!")

print("--------------------------------")
