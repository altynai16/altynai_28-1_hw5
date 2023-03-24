import random
from decouple import config


def casino():
    money = config('MY_MONEY', cast=int)
    my_money = money
    # print(f'Welcom to Casino\nYou have: {my_money}$')
    while True:
        number = input('Put number between 1 and 30: ')
        try:
            number = int(number)
            if number not in range(1, 30):
                print('This number isnt suitable(')
                continue
        except ValueError:
            print('Enter only integers')
            continue

        bet = input('your bet: ')
        try:
            bet = int(bet)
            if bet > my_money:
                print(f'Your bet higher than your balance: {my_money}')
                continue
        except ValueError:
            print('Enter only integers')
            continue

        slot = random.randint(1, 31)
        if slot == number:
            cash = bet * 2
            my_money += cash
            print('Jackpot!!! You win)')
        else:
            my_money -= bet
        again = input('Do you want to continue?: ')
        if again.lower() == 'y':
            continue
        if again.lower() == 'n':
            print(f'Four balance: {my_money}')
            break


if __name__ == '__main__':
    casino()





# 1. Установить в свою виртуальную среду проекта внешний модуль python-decouple
# 2. В файле requirements.txt зафиксировать зависимости проекта с помощью команды pip freeze
# 3. Создать многомодульную игру Казино
# 4. Сам запуск игры в отдельном файле
# 5. Логика выигрыша или проигрыша в отдельном файле
# Правила игры такие :
# A. Есть массив из чисел от 1 до 30, каждый раз вы делаете ставку на определенную слоту из чисел и ставите деньги
# B. Рандомно выбирается выигрышная слота, если вы выигрываете, вам причисляется удвоенная сумма, той которую вы поставили, если вы загадали невыигрышную слоту - теряете поставленную сумму
# C. В начале игры у вас также есть деньги например 1000$, но в конце мы понимаем вы в выигрыше или в проигрыше
# D. значение переменной начального капитала должно считываться с системной переменной под названием MY_MONEY из файла settings.ini
# E. После каждой ставки вам задается вопрос хотите ли вы сыграть еще, если да - то делаете ставку, если нет - то подводится итог игры