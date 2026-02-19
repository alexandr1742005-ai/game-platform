import random


def guess_the_number():
    print("Салют это 'Угадай число'!")
    print("Выберите уровень сложности:")
    print("1. Лёгкий (1–10, 5 попыток)")
    print("2. Средний (1–50, 6 попыток)")
    print("3. Сложный (1–100000, 7 попыток)")

    while True:
        try:
            level = int(input("Ваш выбор (1/2/3): "))
            if level == 1:
                max_num, max_attempts = 10, 5
                break
            elif level == 2:
                max_num, max_attempts = 50, 6
                break
            elif level == 3:
                max_num, max_attempts = 100000, 7
                break
            else:
                print("Введите 1, 2 или 3.")
        except ValueError:
            print("Пожалуйста, введите число.")

    secret = random.randint(1, max_num)
    attempts = 0

    print(f"\nЯ загадал ебанутое число от 1 до {max_num}. У вас {max_attempts} попыток, но ты все равно не угадаешь потому что ты лох")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка {attempts + 1}: "))
            attempts += 1

            if guess == secret:
                print(f"ебать ты угадал за {attempts} попыток!")
                break
            elif guess < secret:
                print("бля маловато!")
            else:
                print("дохуя берешь!")
        except ValueError:
            print("Введите целое число!")
            attempts += 1  # Считаем как попытку

    else:
        print(f"\n😞 лох не угадал: {secret}")

    # Повтор?
    if input("\nСыграть ещё раз? (да/нет): ").lower().startswith('д'):
        guess_the_number()
    else:
        print("Спасибо за игру! ✨")


if __name__ == "__main__":
    guess_the_number()