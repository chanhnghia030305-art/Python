class Question:
    def __init__(self, hint, answer):
        self.hint = hint
        self.answer = answer

questions = [
    Question("Số có 2 chữ số nhỏ hơn 20 vừa chia hết cho 5 vừa chia hết cho 3", 15),
    Question("Số nguyên tố nhỏ nhất lớn hơn 10", 11),
    Question("Số này bằng bình phương của 4", 16)
]

score = 0
for question in questions:
    print(question.hint)
    user_answer = input("Nhập đáp án của bạn: ")
    if user_answer.isdigit and int(user_answer) == question.answer:
        print("Chính xác!\n")
        score += 1
    else:
        print(f"Sai rồi! Đáp án đúng là: {question.answer}\n")

print(f"Bạn đã trả lời đúng {score}/{len(questions)} câu.") 
