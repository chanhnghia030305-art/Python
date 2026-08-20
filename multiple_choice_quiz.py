from quiz import Quiz
questions = [
    "Câu 1. Đội bóng nào đã vô địch World Cup năm 1994?\nA. Brazil\nB. Đức\nC. Argentina\nD. Ý",
    "Câu 2. Đội bóng nào đã vô địch World Cup năm 1998?\nA. Brazil\nB. Pháp\nC. Argentina\nD. Ý",
    "Câu 3. Đội bóng nào đã vô địch World Cup năm 2002?\nA. Brazil\nB. Đức\nC. Argentina\nD. Ý",
]

quizzes = [
    Quiz(questions[0], "A"),
    Quiz(questions[1], "B"),
    Quiz(questions[2], "A")
]

def run_quizzes(quizzes):
    score = 0
    for quiz in quizzes:
        print(quiz.questions)
        user_answer = input("Nhập câu trả lời của bạn (A, B, C, D): ")
        if user_answer.upper() == quiz.answers:
            print("Đúng!")
            score += 1
        else:
            print(f"Sai! Câu trả lời đúng là: {quiz.answers}")
    print(f"\nBạn đã trả lời đúng {score}/{len(quizzes)} câu hỏi.")
        
        
        
run_quizzes(quizzes)
        