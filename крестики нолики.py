def field(board_num):
    print('—' * 17)
    for i in range(3):
        print(f'  {board_num[3*i]}  |  {board_num[3*i + 1]}  |  {board_num[3*i +2]}')
        print('—' * 17)


def add_sign(sign1, number1, board_num):
    board_num[number1-1] = sign1


def check_win(board_num):
    if (board_num[0] == board_num[1] == board_num[2] or board_num[3] == board_num[4] == board_num[5] or
            board_num[6] == board_num[7] == board_num[8] or

            board_num[0] == board_num[3] == board_num[6] or board_num[1] == board_num[4] == board_num[7] or
            board_num[2] == board_num[5] == board_num[8] or

            board_num[0] == board_num[4] == board_num[8] or board_num[2] == board_num[4] == board_num[6]):
        return True


def correct_checker(number, board_num):
    if number > 9 or number < 1:
        print('-' * 100, '\n', '-' * 100)
        print('Введите незанятое число от 1 до 9')
        return False

    if board_num[number-1] == 'X' or board_num[number-1] == '0':
        print('-' * 100, '\n', '-' * 100)
        print('Клетка занята')
        return False

    return True


def game():
    board_num = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    counter = 1

    while True:
        field(board_num)

        if counter % 2 != 0:
            sign = 'X'
            player = 1
        else:
            sign = '0'
            player = 2
        number = input(f'Ход игрока {player}, введите номер клетки, что бы поставить {sign}: ')

        try:
            number = int(number)
        except ValueError:
            print('-' * 100, '\n', '-' * 100)
            print('Введите число')
            continue

        if not correct_checker(number, board_num):
            continue

        add_sign(sign, number, board_num)

        if check_win(board_num):
            print('-' * 100, '\n', '-' * 100)
            field(board_num)
            print(f'Победа игрока: {player}')
            break

        if counter == 9:
            print('-' * 100, '\n', '-' * 100)
            field(board_num)
            print('Ничья')
            break

        counter += 1


while True:
    answer = input('Чтобы начать новую игру нажмите "1": ')

    try:
        answer = int(answer)
    except ValueError:
        print('-' * 100, '\n', '-' * 100)
        print('Введите число')
        continue

    if answer != 1:
        print('-' * 100, '\n', '-' * 100)
        print('Введите "1" что бы начать игру')
        continue

    if answer == 1:
        game()
        continue
