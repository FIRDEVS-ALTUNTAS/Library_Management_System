class Library:
    def __init__(self, file_name):
        self.file = open(file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        # dosyanın başına dönerek okumak için
        self.file.seek(0)
        # dosyadaki satırları okuyup bir liste olarak tutmak için
        books = self.file.read().splitlines()

        # her bir satırı işlemesi için bir döngü yazalım.
        for book in books:
            book_info = book.split(",")
            print(f"Book Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        # Kullanıcıdan kitap bilgileri almak için
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        while True:
            release_year = input("Enter the release year (4 digits): ")
            if len(release_year) == 4 and release_year.isdigit():
                # Doğru formatta girilmişse döngüden çık
                break
            else:
                print("Invalid release year. Please enter a 4-digit year.")
        number_of_pages = input("Enter the number of pages: ")

        # Kullanıcının girdiği kitap bilgilerinden bir dize oluşturur.
        book_info = f"{title},{author},{release_year},{number_of_pages}\n"
        # oluşturulan dizeyi dosyaya ekler.
        self.file.write(book_info)
        # dosyanın eklendiğini bildirir.
        print("Book added successfully.")

    def remove_book(self):
        # Kullanıcıdan silinecek kitabın adını almak için
        book_to_be_removed = input("Enter the name of the book that you want to remove: ")

        # dosyanın içeriğini okur ve her bir satırı bir listeye ekler.
        self.file.seek(0)
        books = self.file.read().splitlines()

        # silinecek olan kitabın adını listede bulmak için
        for book in books:
            book_info = book.split(",")
            if book_info[0] == book_to_be_removed:
                books.remove(book)
                print(f"Book '{book_to_be_removed}' removed.")
                break
        else:
            print(f"Book '{book_to_be_removed}' not found. Try again after checking the name.")

        # dosyanın içeriğini temizlemek için
        self.file.seek(0)
        self.file.truncate()

        # son olarak güncelleşmiş kitap listesini dosyaya yazalım.
        for book in books:
            self.file.write(book + "\n")


# 'lib' adında bir 'Library' nesnesi oluşturduk.
lib = Library("books.txt")

while True:
    # Menüyü gösteriyoruz.
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

    # Kullanıcıdan menü seçeneğini almak için
    menu_choice = input("Enter your choice: ")

    # Kullanıcının seçimine göre ilgili işlemi gerçekleştirmek için
    if menu_choice == "1":
        lib.list_books()
    elif menu_choice == "2":
        lib.add_book()
    elif menu_choice == "3":
        lib.remove_book()
    elif menu_choice.lower() == "q":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid menu item.")

    input("Press Enter to continue...")
