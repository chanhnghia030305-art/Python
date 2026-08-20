def translate(text):
    translation = ""
    for char in text:
        if char.lower() in "áàảãạâấầẩẫậăắằẳẵặ":
            if char.isupper():
                translation += "A"
            else:
                translation += "a"
        else:
            translation += char
    return translation
text = input("Nhập vào văn bản cần dịch: ")
print(translate(text))  # Output: "Tran Minh Sang"