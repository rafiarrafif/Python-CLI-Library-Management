import tabulate as tb
import json

class Book:
    def __init__(self, judul, penulis, isbn, stock = 0):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.stock = stock
    def view(self):
        print(f"Judul : {self.judul}")
        print(f"Penulis : {self.penulis}")
        print(f"ISBN : {self.isbn}")
        print(f"Stock Tersedia : {self.stock}")

print("+------------------------------------------+")
print("|                                          |")
print("|             Sistem Pinjam Buku           |")
print("|                                          |")
print("|     Helmi Arrafif Kanahaya (L0225034)    |")
print("|                                          |")
print("+------------------------------------------+")

list_buku=[
    Book(judul="Laskar Pelangi", penulis="Andrea Hirata", isbn="9786020336201", stock=5),
    Book(judul="Bumi Manusia", penulis="Pramoedya Ananta Toer", isbn="9786020336010", stock=3),
    Book(judul="Negeri 5 Menara", penulis="Ahmad Fuadi", isbn="9786020336225", stock=4),
    Book(judul="Ayat-Ayat Cinta", penulis="Habiburrahman El Shirazy", isbn="9786020336232", stock=2)
]

##### Main Program Loop #####
while True:
    select_menu = input("Pilih Menu\na) Tambah Buku\nb) Tampilkan Buku\nc) Pinjam Buku\nd) keluar\n\nPilih: ").strip().lower()

    if select_menu == "a":
        while True:
            judul = input("Masukan judul buku: ").strip()
            penulis = input("Masukan penulis buku: ").strip()
            isbn = input("Masukan ISBN buku: ").strip()
            stock = input("Masukan stock (kosongkan jika tidak ada): ")
            if judul == "" or penulis == "" or isbn == "" :
                print(f"Input yang kamu masukan tidak valid")
                break
            else:
                list_buku.append(Book(judul=judul, penulis=penulis, isbn=isbn, stock=stock))
                print(f"Buku {judul} telah berhasil ditambahkan")
                break

    if select_menu == "b":
        if len(list_buku) == 0:
            print("Belum ada buku.")
        else:
            print("\nDaftar Buku:")
            data_view = [vars(buku) for buku in list_buku]
            print(tb.tabulate(data_view, headers="keys", tablefmt="fancy_grid"))
            input("Tekan Enter untuk kembali ke menu...")

    if select_menu == "c":
        print("pinjem buku")

    if select_menu == "d":
        print("Sampai jumpa :)")
        break
