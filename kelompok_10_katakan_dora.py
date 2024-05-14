class KatakanPeta():
    def __init__(self):
        self.daftarKota = {}
        self.jumlahKota = 0
        self.peta = {}
    
    def tampilkanKota(self):
        for kota in self.daftarKota:
            print(kota)

        print(f"Jumlah Kota: {self.jumlahKota}")
    
    def tampilkanPeta(self):
        for i, kota in enumerate(self.peta):
            print(f"{i+1}. {kota}")
            for kotaTetangga, rute in self.peta[kota].items():
                print(f"\t--> {kotaTetangga}:")
                for jalan in rute.values():
                    print(f"\t\t--> {jalan}")
    
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

    def buatkanRute(self, start):
        peta = {}

        [distances, routes] = self.dijkstra(start)
        for kota, jarak in distances.items():
            peta[kota] = {}
            peta[kota]["rute"] = self.route(distances, routes, start, kota)
            peta[kota]["jarak"] = jarak

        self.peta[start] = peta

     def cariRuteTercepat(self, dari, ke):
        dari = dari.title()
        ke = ke.title()
        if dari in self.daftarKota and ke in self.daftarKota:
            print(f"\tDari {dari} ke {ke}, berjarak {self.peta[dari][ke]["jarak"]} km")
            print(f"\tDengan rute: ")
            for jalan, jarak in reversed(self.peta[dari][ke]["rute"].items()):
                print("\t\t --->", jalan, jarak, "km")
        else:
            print(f"{dari} atau {ke} tidak berada di daftar kota")
    
    def route(self, distances, routes, start, target):
        path = {}
        city = target
