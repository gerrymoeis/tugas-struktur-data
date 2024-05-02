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
