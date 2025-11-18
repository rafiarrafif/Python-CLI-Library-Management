import tabulate as tb

class Book:
    def __init__(self, judul, penulis, isbn, stock = 0):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.stock = stock

def borrow_book(isbn_target):
    book_found = False
    for book in list_buku:
        if book.isbn == isbn_target:
            book_found = book.judul
            if book.stock == 0:
                return f"Stok buku {book_found} telah habis." 
            book.stock -= 1
    return f"Buku {book_found} berhasil dipinjam." if book_found else f"Buku dengan ISBN {isbn_target} tidak ditemukan."

print("+------------------------------------------+")
print("|                                          |")
print("|             Sistem Pinjam Buku           |")
print("|                                          |")
print("|     Helmi Arrafif Kanahaya (L0225034)    |")
print("|                                          |")
print("+------------------------------------------+")

##### Initation book list #####
'''

'''
list_buku=[
    Book(judul="Laskar Pelangi", penulis="Andrea Hirata", isbn="9786020336201", stock=5),
    Book(judul="Bumi Manusia", penulis="Pramoedya Ananta Toer", isbn="9786020336010", stock=3),
    Book(judul="Negeri 5 Menara", penulis="Ahmad Fuadi", isbn="9786020336225", stock=4),
    Book(judul="Ayat-Ayat Cinta", penulis="Habiburrahman El Shirazy", isbn="9786020336232", stock=2)
]
##### (END) Initation book list #####

##### Main Program Loop #####
while True:
    print("\n"*12)
    select_menu = input("=== Menu Utama ===\na) Tambah Buku\nb) Tampilkan Buku\nc) Pinjam Buku\nd) keluar\n\nPilih: ").strip().lower()

    ##### Add new book #####
    if select_menu == "a":
        while True:
            judul = input("Masukan judul buku: ").strip()
            penulis = input("Masukan penulis buku: ").strip()
            isbn = input("Masukan ISBN buku: ").strip()
            stock = input("Masukan stock (kosongkan jika tidak ada): ")
            if judul == "" or penulis == "" or isbn == "" :
                print("Input yang kamu masukan tidak valid")
                input("Tekan Enter untuk melanjutkan...")
                break
            elif not stock.isdigit():
                print("Stock harus berupa angka")
                input("Tekan Enter untuk melanjutkan...")
                break
            else:
                list_buku.append(Book(judul=judul, penulis=penulis, isbn=isbn, stock=int(stock) if stock else 0))
                print(f"Buku {judul} telah berhasil ditambahkan")
                input("Tekan Enter untuk melanjutkan...")
                break
    ##### (END) Add new book #####

    ##### View book list #####
    if select_menu == "b":
        if len(list_buku) == 0:
            print("Belum ada buku.")
        else:
            print("\nDaftar Buku:")
            data_view = [vars(buku) for buku in list_buku]
            print(tb.tabulate(data_view, headers="keys", tablefmt="fancy_grid"))
            input("Tekan Enter untuk kembali ke menu...")
    ##### (END) View book list #####

    ##### Borrow book #####
    if select_menu == "c":
        isbn_target = input("Masukan ISBN buku yang ingin dipinjam: ").strip()
        print(borrow_book(isbn_target))
        input("Tekan Enter untuk kembali ke menu...")
    ##### (END) Borrow book #####

    if select_menu == "d":
        print("Sampai jumpa :)")
        break
##### (END) Main Program Loop #####
