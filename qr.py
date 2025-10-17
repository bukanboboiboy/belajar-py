import qrcode

# Link yang ingin diubah menjadi QR code
url = "https://img-9gag-fun.9cache.com/photo/a9dERVK_700bwp.webp"

# Membuat QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Membuat gambar QR code
img = qr.make_image(fill_color="black", back_color="white")

# Menyimpan gambar QR code
img.save("qr_link.png")