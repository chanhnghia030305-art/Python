class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

flashcards = [
    Flashcard("Coffee", "Cà phê"),
    Flashcard("Tea", "Trà"),
    Flashcard("Ball", "Bóng")
]
score = 0
for flashcard in flashcards:
    print(f"Nghĩa của từ {flashcard.word} là gì?")
    user_meaning = input("Nhập đáp án của bạn: ")
    if user_meaning.strip().lower() == flashcard.meaning.strip().lower():
        print("Đúng!")
        score += 1
    else:
        print("Sai!")

print(f"Bạn đã trả lời đúng {score}/{len(flashcards)}")

