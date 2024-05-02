"""
    Kelompok 10_2023E - Kumpulan Tugas Struktur Data
    
    1. Gerry Moeis M.D.P - 23091397164 (Ketua)
    2. Ahmad Aryobimo - 23091397151 (Notulis)
    3. Dea Ayu Novita Putri - 23091397173 (Editor)
"""

class KatakanPeta():
    def __init__(self):
        self.daftarKota = {}
        self.jumlahKota = 0
    
    def tampilkanPeta(self):
        for kota in self.daftarKota:
            print(f"{kota} -> {self.daftarKota[kota]}")
        print(f"Jumlah Kota: {self.jumlahKota}")
    
    def tambahkanKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
            self.jumlahKota += 1
    
    def tambahkanJalan(self, kota1, cities):
        for kota in cities:
            if kota1 and kota in self.daftarKota:
                self.daftarKota[kota1][kota] = cities[kota]
                self.daftarKota[kota][kota1] = cities[kota]
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
            self.jumlahKota -= 1
    
    def hapusJalan(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]
    
    def cariRuteTercepat(self, kota):
        kota = kota.title()
        if kota in self.daftarKota:
            terdekat = min(self.daftarKota[kota].values())
            rute = [jalan for jalan in self.daftarKota[kota] if self.daftarKota[kota][jalan] == terdekat]
            print(", ".join([f"{jalan} {terdekat}km" for jalan in rute]))
        else:
            print(f"{kota} tidak berada di daftar kota")

cities = ["Amsterdam", "Almere", "Amersfoort", "Utrecht", "Vianen", "Gouda", "Rotterdam", "Delft", "Den Haag", "Leiden", "Haarlem"]

petaBelanda = KatakanPeta()
for city in cities:
    petaBelanda.tambahkanKota(city)
    
petaBelanda.tambahkanJalan("Amsterdam", {"Haarlem": 31.7, "Leiden": 49.6, "Almere": 32.3})
petaBelanda.tambahkanJalan("Den Haag", {"Leiden": 33, "Delft": 13})
petaBelanda.tambahkanJalan("Gouda", {"Delft": 35.8, "Rotterdam": 23.7, "Utrecht": 40.9})
petaBelanda.tambahkanJalan("Utrecht", {"Gouda": 40.9, "Vianen": 18.2, "Amersfoort": 24.4})
petaBelanda.tambahkanJalan("Almere", {"Amsterdam": 32.3, "Amersfoort": 42})
