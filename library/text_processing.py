"""
coba = "Bukan Boboiboy"
besar = coba.upper()
kecil = coba.lower()
judul = coba.title()
bagi = coba.split("b")
tambah_nol = coba.zfill(20)
print(besar)
print(kecil)
print(judul)
print(bagi)
print(tambah_nol)
"""

import re

pola = '^i... ....k$'
name = 'isra malik'

hasil = re.match(pola, name)

if hasil:
    print("match")

else:
    print("not match")
