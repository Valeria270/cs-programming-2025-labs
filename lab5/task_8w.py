import random
def rock_paper_scissors_lizard_spock():
    options = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']

    rules = {
        'камень': ['ножницы', 'ящерица'],
        'ножницы': ['бумага', 'ящерица'],
        'бумага': ['камень', 'спок'],
        'ящерица': ['спок', 'бумага'],
        'спок': ['ножницы', 'камень']
    }

    win_messages = {
        ('камень', 'ножницы'): 'Камень разбивает ножницы',
        ('камень', 'ящерица'): 'Камень давит ящерицу',
        ('ножницы', 'бумага'): 'Ножницы режут бумагу',
        ('ножницы', 'ящерица'): 'Ножницы обезглавливают ящерицу',
        ('бумага', 'камень'): 'Бумага покрывает камень',
        ('бумага', 'спок'): 'Бумага подставляет Спока',
        ('ящерица', 'спок'): 'Ящерица отравляет Спока',
        ('ящерица', 'бумага'): 'Ящерица съедает бумагу',
        ('спок', 'ножницы'): 'Спок ломает ножницы',
        ('спок', 'камень'): 'Спок испаряет камень'
    }

    print("=" * 50)
    print("Игра: Камень-Ножницы-Бумага-Ящерица-Спок")
    print("=" * 50)
    print("Доступные варианты: камень, ножницы, бумага, ящерица, спок")
    print("Для выхода введите 'выход'")
    print("=" * 50)

    while True:
        user_choice = input("\nВаш выбор: ").lower().strip()

        # Проверка на выход
        if user_choice in ['выход', 'exit', 'quit']:
            print("Спасибо за игру!")
            break

        if user_choice not in options:
            print("Ошибка: выберите один из вариантов:", ", ".join(options))
            continue

        computer_choice = random.choice(options)

        print(f"\nВаш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        print("-" * 30)

        if user_choice == computer_choice:
            print("Ничья!")
        elif computer_choice in rules[user_choice]:
            message = win_messages.get((user_choice, computer_choice),
                                       f"{user_choice.capitalize()} побеждает {computer_choice}")
            print(f"{message}")
            print("Вы победили!")
        else:
            message = win_messages.get((computer_choice, user_choice),
                                       f"{computer_choice.capitalize()} побеждает {user_choice}")
            print(f"{message}")
            print("Победил компьютер!")

if __name__ == "__main__":
    rock_paper_scissors_lizard_spock()