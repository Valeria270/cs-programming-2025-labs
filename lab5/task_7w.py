eng_to_rus = {
    "apple": "яблоко",
    "cat": "кошка",
    "dog": "собака",
    "house": "дом",
    "book": "книга"
}

word = input("Введите русское слово: ")

found = False
for eng, rus in eng_to_rus.items():
    if rus == word:
        print(f"Перевод на английский: {eng}")
        found = True
        break

if not found:
    print("Перевод не найден")