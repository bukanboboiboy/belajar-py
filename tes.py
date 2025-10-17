"""
### ini namanya dekorator (method biasa)

def intro(umur):
    def salam():
        print("Halo, nama saya John.")
        umur()
    return salam

@intro
def umur():
    print("Umur saya 17 tahun.")

umur()
### ini namanya  Static method (yang tidak membutuhkan self)
class Mobil:
    def __init__(self, merek):
        self.merek = merek
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("Toyota")
mobil_1.intro_mobil()
print(mobil_1.merek)

### ini namanya  Class Method (yang membutuhkan cls)

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("Toyota")
mobil_1.intro_mobil()
print(mobil_1.merek)


### pewarisan (inheritance)
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        self.jumlah_roda = 4
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

mobil_sport_1 = Mobil("Kuning", "Civic", 200)
print(mobil_sport_1.kecepatan)
print(mobil_sport_1.jumlah_roda)
Mobil.jumlah_roda = 2
print(Mobil.jumlah_roda)
print(mobil_sport_1.jumlah_roda)
print(mobil_1.jumlah_roda)
mobil_sport_2 = Mobil("Biru", "Ferrari", 300)
print(mobil_sport_2.jumlah_roda)
mobil_sport_1.jumlah_roda=2
print(mobil_sport_1.jumlah_roda)
"""


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species


class Cat(Animal):
    def deskripsi(self):
        return (
            f"{self.name} adalah kucing berjenis {self.species} "
            f"yang sudah berumur {self.age} tahun"
        )

    def suara(self):
        return "Meow"


my_cat = Cat("Neko", 3, "Persian")

print(my_cat.deskripsi())
print("Dia bersuara", my_cat.suara())