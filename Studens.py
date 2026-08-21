class Sinh_Vien:
    def __init__(self, name, score):
        self.name = name
        self.score = score

studens = [
    Sinh_Vien("Nguyen Van A", 8.5),
    Sinh_Vien("Nguyen Van B", 7.5),
    Sinh_Vien("Nguyen Van C", 9.0),
    Sinh_Vien("Nguyen Van D", 6.5)
]

total = 0
for student in studens:
    print(f"Name: {student.name}, Score: {student.score}")
    total += student.score

average = total / len(studens)
print(f"Average score: {average}")