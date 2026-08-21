class Sinh_Vien:
    def __init__(self, name, score):
        self.name = name
        self.score = score

names = [
    Sinh_Vien("Nghĩa", 9),
    Sinh_Vien("Huy", 8),
    Sinh_Vien("Hoàng", 10)
]
total = 0
for Sinh_Vien in names:
    print(f"{Sinh_Vien.name}: {Sinh_Vien.score}")
    total += Sinh_Vien.score

average = total / len(names)
print(f"\nĐiểm trung bình cả lớp: {average:.2f}")

