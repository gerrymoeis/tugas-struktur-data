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
