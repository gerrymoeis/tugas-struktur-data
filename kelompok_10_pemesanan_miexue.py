from kelompok_10_linked_list import LinkedList

class DaftarPesanan(LinkedList):
    def __init__(self, data=None):
        super().__init__(data)
        self.message = "Daftar Pesanan Masih Kosong, Yok Belanja"
    
    def tampilkan_menu(self, menus, message="Silahkan dipilih menunya (input 'nomer'nya): "):
        print(menus)
        pesanan = input(message)
        return int(pesanan) - 1 if pesanan.isnumeric() else pesanan
    
    def tambahkan_pesanan(self, data):
        self.append(data)
        print(f"{data.nama_menu} ditambahkan ke keranjang")
    
    def rincian_pesanan(self, list_menu):
        rincian = []
        node = self.head
        while node:
            rincian.append(node.data.id)
            node = node.next
        rincian_set = set(rincian)
        
        print("\nRincian Pesanan Anda: ")
        for i, pesanan in enumerate(rincian_set):
            nama_menu, harga = list_menu[pesanan]
            print(f"{i + 1}. {nama_menu} - Rp{harga}: {rincian.count(pesanan)}x = Rp{rincian.count(pesanan) * harga}")
    
    def total_pesanan(self):
        total = 0
        node = self.head
        while node:
            total += node.data.harga
            node = node.next
        
        print(f"Total Harga Pesanan: Rp{total}\nTerima kasih telah memesan")

class Pesanan:
    def __init__(self, id, nama_menu, harga):
        self.id = id
        self.nama_menu = nama_menu
        self.harga = harga
    
    def __str__(self):
        return f"{self.id + 1}. {self.nama_menu.title()} - Rp{self.harga}"

MIXUE_CABANG_MI = {
    "Mixue Ice Cream": 5_000,
    "Boba Shake": 16_000,
    "Mi Sundae": 14_000,
    "Mi Ganas": 11_000,
    "Creamy Mango Boba": 22_000,
}

list_menu = list(MIXUE_CABANG_MI.items())

menus = ""
for i, menu in enumerate(list_menu):
    menus += f"\n{i+1}. {menu[0]} - Rp{menu[-1]}"

daftar_pesanan = DaftarPesanan()

first = True
while True:
    pesanan = daftar_pesanan.tampilkan_menu(menus) if first else daftar_pesanan.tampilkan_menu(menus, message="Ada lagi? (ketik 'exit' untuk mengakhiri pesanan): ")
    if pesanan == "exit":
        break
    elif pesanan not in range(0, len(list_menu)):
        print("Pesanan yang dipilih tidak ada di Menu (input salah)")
        continue
    first = False
    daftar_pesanan.tambahkan_pesanan(Pesanan(pesanan, list_menu[pesanan][0], list_menu[pesanan][-1]))

if daftar_pesanan.length() <= 0:
    print(f"Terima kasih telah berkunjung")
else:
    daftar_pesanan.rincian_pesanan(list_menu)
    daftar_pesanan.total_pesanan()
