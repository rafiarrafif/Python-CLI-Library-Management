import tabulate as tb

##### Define book class #####
class Book:
    def __init__(self, judul, penulis, isbn, stock = 0):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.stock = stock
##### (END) Define book class #####

##### Initation book list and seed dummy data #####
list_buku=[
    Book(judul="Laskar Pelangi", penulis="Andrea Hirata", isbn="9786020336201", stock=5),
    Book(judul="Bumi Manusia", penulis="Pramoedya Ananta Toer", isbn="9786020336010", stock=3),
    Book(judul="Negeri 5 Menara", penulis="Ahmad Fuadi", isbn="9786020336225", stock=4),
    Book(judul="Ayat-Ayat Cinta", penulis="Habiburrahman El Shirazy", isbn="9786020336232", stock=2)
]
##### (END) Initation book list and seed dummy data #####

##### Find book with ISBN function #####
def find_book_from_isbn(isbn_target):
    book_found = False;
    for book in list_buku:
        if book.isbn == isbn_target:
            book_found = book
    return book_found
##### (END) Find book with ISBN function #####


##### Add book function #####
def add_book():
    judul = ""
    penulis = ""
    isbn = ""
    stock = 0
    while True:
        judul = input("Masukan judul buku: ").strip()
        if judul == "":
            print("Judul buku tidak boleh kosong")
        else:
            break
    while True:
        penulis = input("Masukan penulis buku: ").strip()
        if penulis == "":
            print("Penulis buku tidak boleh kosong")
        else:
            break    
    while True:
        isbn = input("Masukan ISBN buku: ").strip()
        checking_isbn = find_book_from_isbn(isbn)
        if isbn == "":
            print("ISBN buku tidak boleh kosong")
        elif checking_isbn:
            print(f"ISBN {checking_isbn.isbn} sudah tercantum pada buku {checking_isbn.judul}. Gunakan yang lain!")
        else:
            break
    while True:
        stock_raw = input("Masukan stock (kosongkan jika tidak ada): ")
        if not stock_raw.isdigit():
            print("Stock harus berupa angka atau dikosongkan.")
        else:
            stock = int(stock_raw) if stock_raw else 0
            break
    print(f"Buku {judul} berhasil ditambahkan.")
    list_buku.append(Book(judul=judul, penulis=penulis, isbn=isbn, stock=stock))
##### (END) Add book function #####

##### Borrow book function #####
def borrow_book(isbn_target):
    book = find_book_from_isbn(isbn_target)
    if book:
        if book.stock == 0:
            return f"Stok buku {book.judul} telah habis." 
        book.stock -= 1
        return f"Buku {book.judul} berhasil dipinjam."
    else:
        return f"Buku dengan isbn {isbn_target} tidak ditemukan."
##### (END) Borrow book function #####

##### Program Header #####
print("+------------------------------------------+")
print("|                                          |")
print("|             Sistem Pinjam Buku           |")
print("|                                          |")
print("|     Helmi Arrafif Kanahaya (L0225034)    |")
print("|                                          |")
print("+------------------------------------------+")
##### (END) Program Header #####

##### Main Program Loop #####
first_run = True
while True:
    print("\n"*99 if first_run == False else "") 
    select_menu = input("=== Menu Utama ===\na) Tambah Buku\nb) Tampilkan Buku\nc) Pinjam Buku\nd) keluar\n\nPilih: ").strip().lower()
    first_run = False

    ##### Add new book #####
    if select_menu == "a":
        add_book()
        input("Tekan Enter untuk kembali ke menu...")
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

    ##### Kill program #####
    if select_menu == "d":
        print("Sampai jumpa :)")
        break
    ##### (END) Kill program #####
##### (END) Main Program Loop #####
