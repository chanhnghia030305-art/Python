phone_book = open("D:\\Text\\phone_book.txt", "r", encoding="utf-8")


for person in phone_book.readlines():
    person = person.replace("\n", "")
    print(person)

phone_book.close()
