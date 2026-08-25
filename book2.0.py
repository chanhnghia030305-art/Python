class Book:
    def __init__(self, title, borrowed):
        self.title = title
        self.borrowed = borrowed


books = [
    Book("Python cơ bản", False),
    Book("Số Đỏ", False),
    Book("Nhà Giả Kim", True),
]
# True: đã được mượn, False: Có sẵn

def show_books(books):
    print("\n--- DANH SÁCH SÁCH ---")
    for book in books:
        status = "📕 Đang được mượn" if book.borrowed else "📗 Có sẵn"
        print(f"{book.title}: {status}")


def borrow_book(books):
    book_name = input("Nhập tên sách muốn mượn: ")
    for book in books:
        if book.title.lower().strip() == book_name.lower().strip():
            if book.borrowed:
                print(f"'{book.title}' hiện đã có người mượn rồi!")
            else:
                book.borrowed = True
                print(f"Bạn đã mượn thành công '{book.title}'!")
            break
    else:
        print("Không tìm thấy sách trong thư viện!")


def return_book(books):
    book_name = input("Nhập tên sách muốn trả: ")
    for book in books:
        if book.title.lower().strip() == book_name.lower().strip():
            if book.borrowed:
                book.borrowed = False
                print(f"'{book.title}' đã được trả lại!")
            else:
                print(f"'{book.title}' chưa được cho mượn!")
            break
    else:
        print("Không tìm thấy sách trong thư viện!")


def main():
    while True:
        print("\n===== MENU THƯ VIỆN =====")
        print("1. Xem danh sách sách")
        print("2. Mượn sách")
        print("3. Trả sách")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            show_books(books)
        elif choice == "2":
            borrow_book(books)
        elif choice == "3":
            return_book(books)
        elif choice == "4":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")


main()