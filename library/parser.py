"""
import argparse
from datetime import datetime, timedelta

current_datetime = datetime.now()
past_date = current_datetime - timedelta(days=(30 * 365))
formatted_past_day = past_date.strftime("%d-%m-%Y")

parser = argparse.ArgumentParser()

parser.add_argument(
    '-n',
    '--NAMAKITA',
    required=True,
    help="Masukkan Nama Anda")
parser.add_argument(
    '-t',
    '--tanggallahir',
    required=True,
    help="Masukkan Tanggal Lahir Anda dengan format dd-mm-yyyy")

args = parser.parse_args()

args.tanggallahir = args.tanggallahir.strip()


if args.tanggallahir < str(formatted_past_day):
    print(
        "Terima kasih telah menggunakan panggildicoding.py,",
        "Mas",
        args.NAMAKITA)
else:
    print(
        "Terima kasih telah menggunakan panggildicoding.py,",
        "Bapak",
        args.NAMAKITA)
"""

import argparse
from datetime import datetime

# --- Tahap 1: Siapkan Parser untuk Menerima Perintah ---
# Bagian ini sudah benar di kode Anda! Excellent work.
parser = argparse.ArgumentParser(
    description="Menyapa pengguna berdasarkan usia.")

parser.add_argument(
    '-n', '--nama',
    required=True,
    help="Masukkan Nama Anda"
)

parser.add_argument(
    '-t', '--tanggallahir',
    required=True,
    help="Masukkan Tanggal Lahir Anda dengan format dd-mm-yyyy"
)

args = parser.parse_args()

# --- Tahap 2: Konversi Input String Menjadi Objek Datetime ---
# Ini adalah langkah paling krusial yang hilang.
# Kita gunakan datetime.strptime (string parse time) untuk mengubah teks
# menjadi tanggal.
try:
    tanggal_lahir_obj = datetime.strptime(args.tanggallahir, "%d-%m-%Y")
except ValueError:
    print("Error: Format tanggal salah. Harap gunakan dd-mm-yyyy.")
    exit()  # Hentikan program jika format tanggal salah

# --- Tahap 3: Hitung Usia ---
# Dapatkan tanggal hari ini
tanggal_hari_ini = datetime.now()
# Hitung selisih waktu antara sekarang dan tanggal lahir
selisih_waktu = tanggal_hari_ini - tanggal_lahir_obj
# Konversi selisih waktu (dalam hari) menjadi tahun
# Kita bagi dengan 365.25 untuk memperhitungkan tahun kabisat
usia_tahun = selisih_waktu.days / 365.25

# --- Tahap 4: Logika Panggilan Berdasarkan Usia ---
# Sekarang kita bisa membandingkan usia (angka) dengan 30.
if usia_tahun < 30:
    panggilan = "Kakak"
else:
    panggilan = "Bapak"

# --- Tahap 5: Tampilkan Hasil ---
# Menggunakan f-string agar lebih rapi
print(
    f"Terima kasih telah menggunakan panggildicoding.py, {panggilan} {
        args.nama}")
