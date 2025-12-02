import time
from file_handler import get_random_word
from game import live
from game import coded
from decorators import timee
# print("ПОЛЕ ЧУДЕС\nВаш лучший рекорд: 0\nВыберите уровень сложности:\n1. Легкий (7 жизней)\n2. Средний (5 жизней)\n3. Сложный (3 жизни)")
# difficulty = int(input("Ваш выбор: "))
# attempts = {1: 7, 2: 5, 3: 3}[difficulty]
#print(len(get_random_word("C:Users/chich/OneDrive/Рабочий стол/wheel_of_fortune/data/words.txt"))*"\u25A0")
print('Это Поле Чудес! Удачной игры!')
def end_game(record, start_time):
    with open('data/records.txt') as file:
            c = file.readline()
    end_time = time.time()
    print(f'Игра вавершена!\n' \
    f'Угадано слов: {record} из 15\n' \
    f'Время игры: {timee(int(end_time - start_time))} \n' \
    f'Ваш лучший рекорд: {c}'
    )
def start_game():
    start_time = time.time()
    word = get_random_word("data/words.txt")
    guessed_letters = set()
    record = 0
    print(
        'Выберите уровень сложности \n1. Лёгкий уровень: 7 жизней\n2. Средний уровень: 5 жизней.\n3. Сложный уровень: 3 жизни.\n(Напишите 1, 2 или 3) ')
    difficult = input("Ваш выбор: ")
    while not difficult.isdigit() or difficult not in ['1', '2', '3']:
        print('Введите число 1, 2 или 3! Попробуйте еще раз!')
        difficult = input()

    attempts = {'1': 7, '2': 5, '3': 3}[difficult]

    while attempts > 0:
        
        print(f'Слово: {coded(word, guessed_letters)}')
        print(f'Количество жизней: {live(attempts)}')
        #print((coded(word, guessed_letters)).replace(' ', ''))

        letter_choice = input('Введите букву или слово целиком: ').lower()

        if not letter_choice.isalpha():
            print('Пожалуйста, введите букву или слово целиком!')
            continue

        if letter_choice in guessed_letters:
            print('Вы уже использовали эту букву!')
            continue

        if letter_choice == word or str(coded(word, guessed_letters).replace(' ', ''))==word:
            print(f'\nПоздравляем! Вы угадали слово {word}! Приз в студию!')
            record += 1
            save_record(record)

            user_choice = input(
                f'Ваш рекорд: {record}! \nЖелаете ли вы пойти дальше? \n(Напишите Да или Нет) \nВаш выбор: ').lower()
            while user_choice not in ['да', 'нет']:
                print('Введите Да или Нет! Попробуйте еще раз!')
                user_choice = input('Ваш выбор: ').lower()

            if user_choice == 'да':
                word = get_random_word("data/words.txt")
                guessed_letters.clear()
                attempts = {'1': 7, '2': 5, '3': 3}[difficult]
            else:
                end_game(record, start_time)
                break
        elif len(letter_choice) == 1:
            guessed_letters.add(letter_choice)
            if letter_choice in word:
                print(f'Вы угадали букву: {letter_choice}! Поздравляем!')
            else:
                print('Неправильно! Попробуйте еще раз!')
                attempts -= 1
        else:
            print('Неправильно! Попробуйте еще раз!')
            attempts -= 1
        if record == 15:
            end_game(record, start_time)
            break

    else:
        print(f'\nУ вас не осталось попыток. Загаданное слово было: {word}')
        end_game(record, start_time)

def save_record(record):
    try:
        with open('data/records.txt', mode='r', encoding='utf8') as file:
            current_record = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        current_record = 0

    if record > current_record:
        with open('data/records.txt', mode='w', encoding='utf8') as file:
            file.write(str(record))
        print('Ваш рекорд сохранён/обновлён!')

start_game()