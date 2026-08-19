secret_word = "Python"
hint = "Gợi ý: Đây là một ngôn ngữ lập trình phổ biến."
guess = ""
guess_count = 0
guess_limit = 3
print("Chào mừng bạn đến với trò chơi đoán từ bí mật!")
print(hint)
while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Hãy đoán từ bí mật: ")
        guess_count += 1
    else:
        break

if guess == secret_word:
    print("Chúc mừng! Bạn đã đoán đúng từ bí mật.")
else:
    print("Rất tiếc! Bạn đã hết lượt đoán. Từ bí mật là:", secret_word)
    