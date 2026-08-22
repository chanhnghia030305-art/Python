class Book:
    def __init__(self, title, borrowed):
        self.title = title
        self.borrowed = borrowed


books = [
    Book("Python cơ bản", False),
    Book("Số Đỏ", False),
    Book("Nhà Giả Kim", True),
]

# In danh sách sách ban đầu
for book in books:
    status = "📕 Đang được mượn" if book.borrowed else "📗 Có sẵn"
    print(f"{book.title}: {status}")

print()

# Người dùng nhập tên sách muốn mượn
book_name = input("Nhập tên sách muốn mượn: ")

for book in books:
    if book.title == book_name:
        if book.borrowed:
            print(f"'{book.title}' hiện đã có người mượn rồi!")
        else:
            book.borrowed = True   # <-- cập nhật thuộc tính, giống task.done = True
            print(f"Bạn đã mượn thành công '{book.title}'!")
        break
else:
    print("Không tìm thấy sách này trong thư viện.")

print()

# In lại danh sách sau khi cập nhật
for book in books:
    status = "📕 Đang được mượn" if book.borrowed else "📗 Có sẵn"
    print(f"{book.title}: {status}")
    
    
# Người mượn trả sách
book_name = input("Nhập tên sách muốn trả: ")

for book in books:
    if book.title == book_name:
        if book.borrowed:
            book.borrowed = False
            print(f"'{book.title}' đã được trả lại!")
        else:
            print(f"'{book.title}' chưa được cho mượn!")
        break

else:
    print("Không tìm thấy sách trong thư viện!")
    
print()
for book in books:
    status = "📕 Đang được mượn" if book.borrowed else "📗 Có sẵn"
    print(f"{book.title}: {status}")