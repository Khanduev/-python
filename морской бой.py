import copy
import random


def field(game_field):
    print('—' * 44)
    print(f'   | а | б | в | г | д | е | ж | з | и | к |')
    print('—' * 44)

    for i in range(1, len(game_field)-1):  # вывод внутреннего поля 10*10 из поля 12*12
        if i < 10:
            print('', i, end=' | ')
        else:
            print(i, end=' | ')  # красивое отображение двузначного числа строки поля

        for j in range(1, len(game_field[i])-1):
            print(game_field[i][j], end=' | ')
        print()


def add_ship(game_field):  # добавляет корабли
    ship_type = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for ship in ship_type:
        while True:
            direction = random.randint(0, 1)  # выбор направления корабля
            if direction == 0:
                row = random.randint(1, 10)
                col = random.randint(1, 11 - ship)
                k1 = 0  # коэффициенты необходимые для перемещения клеток корабля
                k2 = 1
            else:
                row = random.randint(1, 11 - ship)
                col = random.randint(1, 10)
                k1 = 1
                k2 = 0

            #  проверка каждой клетки на незанятость и проверка ореола, если проверка пройдена ставит 4 клетки корабля
            if ship == 4:
                if (check_cell(game_field, row, col) and check_cell(game_field, row + 1*k1, col + 1*k2) and
                        check_cell(game_field, row + 2*k1, col + 2*k2) and
                        check_cell(game_field, row + 3*k1, col + 3*k2)):
                    game_field[row][col] = "■"
                    game_field[row + 1*k1][col + 1*k2] = "■"
                    game_field[row + 2*k1][col + 2*k2] = "■"
                    game_field[row + 3*k1][col + 3*k2] = "■"
                    break

            if ship == 3:
                if (check_cell(game_field, row, col) and check_cell(game_field, row + 1*k1, col + 1*k2) and
                        check_cell(game_field, row + 2*k1, col + 2*k2)):
                    game_field[row][col] = "■"
                    game_field[row + 1*k1][col + 1*k2] = "■"
                    game_field[row + 2*k1][col + 2*k2] = "■"
                    break

            if ship == 2:
                if check_cell(game_field, row, col) and check_cell(game_field, row + 1*k1, col + 1*k2):
                    game_field[row][col] = "■"
                    game_field[row + 1*k1][col + 1*k2] = "■"
                    break

            if ship == 1:
                if check_cell(game_field, row, col):
                    game_field[row][col] = "■"
                    break

    return game_field


# Проверка свободности клеток в месте установки и вокруг
def check_cell(game_field, row, col):
    if (game_field[row][col] != "■" and game_field[row-1][col] != "■" and game_field[row-1][col-1] != "■" and
            game_field[row][col-1] != "■" and game_field[row+1][col-1] != "■" and game_field[row+1][col] != "■" and
            game_field[row+1][col+1] != "■" and game_field[row][col+1] != "■" and game_field[row-1][col+1] != "■"):
        return True


def check_buoyancy_ship(game_field, row, col):  # проверка наличия частей корабля
    sign = ["■", 'X']

    # проверка направления корабля (верт. или гор.) с установкой коэффициентов
    if game_field[row - 1][col] in sign or game_field[row + 1][col] in sign:
        k1 = 1
        k2 = 0
    elif game_field[row][col - 1] in sign or game_field[row][col + 1] in sign:
        k1 = 0
        k2 = 1
    else:  # если вокруг нет других частей корабля то корабль однопалубый и он потоплен
        return True

    # Проверка потопления корабля совершается в два этапа, проверяется верхнаяя или левая часть корабля от места
    # попадания, потом слева на право или сверху вниз.
    # Если сверху или слева от точки попадания есть часть корабля или попадание по кораблю то через цикл передвигаем
    # туда точку, если в точке есть целая часть корабля то выдаем False, если есь попадание, то передвигаем точку еще
    # вверх или влево, если клетка не ни что их предадущего, то завершаем цикл
    if game_field[row - 1 * k1][col - 1 * k2] in sign:
        print('tut5')
        while True:  # перестановка точки последнего удара в левый верхний угол, за 4 хода
            if game_field[row - 1 * k1][col - 1 * k2] == "X":
                row -= 1 * k1
                col -= 1 * k2
            elif game_field[row - 1 * k1][col - 1 * k2] == "■":
                return False
            else:
                break

    # аналогично верхнему, только проверка идет в право или вниз
    if game_field[row + 1 * k1][col + 1 * k2] in sign:
        print('tut6')
        while True:
            if game_field[row + 1 * k1][col + 1 * k2] == "X":
                row += 1 * k1
                col += 1 * k2
            elif game_field[row + 1 * k1][col + 1 * k2] == "■":
                return False
            else:
                break

    return True  # если все проверкаи пройдены, то корабля потоплен


def halo_ship(game_field, row, col):  # установка ореола после уничтожения корабля
    for i in range(4):  # перестановка точки последнего удара в левый верхний угол, за 4 хода
        if game_field[row - 1][col] != "X":
            game_field[row - 1][col] = "."
        else:
            row = row - 1  # смещение строки карты на один вверх
        if game_field[row][col - 1] != "X":
            game_field[row][col - 1] = "."
        else:
            col = col - 1
    # установка ореола уничтоженного корабля сначала по диагоналям, затем по вертикали и горизонтали
    # проверка клетки на наличие части уничтоженного корабля и продвижение в правый нижний угол карты
    for i in range(4):
        game_field[row - 1][col - 1] = "."
        game_field[row - 1][col + 1] = "."
        game_field[row + 1][col - 1] = "."
        game_field[row + 1][col + 1] = "."

        if game_field[row + 1][col] != "X":
            game_field[row + 1][col] = "."
        else:
            row = row + 1
        if game_field[row][col + 1] != "X":
            game_field[row][col + 1] = "."
        else:
            col = col + 1


def hide_ship(game_field):  # замена клеток с кораблями на пустые
    hide_game_field = game_field.copy()

    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == '■':
                hide_game_field[i][j] = ' '

    return hide_game_field


#  проверка количества оставшихся кораблей(частей кораблей)
def check_ship(game_field):
    for i in game_field:  # если есть корабль, то возвращается True
        if '■' in i:
            return False
    return True


# проверка поля игрока на наличие промахов и попаданий и составление массива списков с индексами колонок для последующей
# стрельбы
def field_player_for_pc(game_field):
    new_field = []
    for i in range(1, 11):
        b = []
        for j in range(1, 11):
            if game_field[i][j] != '.' and game_field[i][j] != 'X':
                b.append(j)
        new_field.append(b)
    return new_field


def game():
    # поле задается 12*12, что бы удобнее проводить проверку ореола кораблей
    game_field = [[' ' for j in range(12)] for i in range(12)]
    game_field2 = [[' ' for j in range(12)] for i in range(12)]

    player_field = add_ship(game_field)
    pc_field = add_ship(game_field2)

    count = 0
    while True:
        if check_ship(player_field):
            field(player_field)
            field(pc_field)
            print('Игра окончена')
            print('Победил ПК')
            break
        count += 1
        print('—' * 100)
        print(f'ход номер: {count}')
        print('Поле игрока:')
        field(player_field)
        print()
        print('Поле компьютера:')
        hide_game_field = copy.deepcopy(pc_field)  # создание копии поля противника
        hide_ship(hide_game_field)  # скрытие кораблей противника
        field(hide_game_field)  # показ поля противника со скрытыми кораблями
        print()

        while True:
            coord = input('введите две координаты в формате "а 1": ').split()

            word = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']
            digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            if len(coord) != 2:  # проверка на количество координат
                print('введите 2 координаты')
                continue
            if coord[0] not in word:  # проверка допустимого значения координат
                print('введите первую координату букву: "а, б, в, г, д, е, ж, з, и, к"')
                continue
            if coord[1] not in digit:
                print('введите первую координату цифру: "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"')
                continue
            break

        alp = 'абвгдежзик'
        coord1 = int(coord[1])  # координаты хода игрока
        coord2 = alp.index(coord[0])+1

        if pc_field[coord1][coord2] == '■':  # проверка попадания по кораблю
            pc_field[coord1][coord2] = 'X'  # если попадание есть, то меняем ■ на Х
            # если функция проверки наличия в округе кораблей показывает их отсутсвие, то переходим в функцию
            # отрисовки ореола потопленного корабля
            if check_buoyancy_ship(pc_field, coord1, coord2):
                print('Вражеский корабль потоплен')
                halo_ship(pc_field, coord1, coord2)
                if check_ship(pc_field):
                    field(player_field)
                    field(pc_field)
                    print('Игра окончена')
                    print('Победил игрок')
                    break
                continue
            else:
                print('Попадание. Еще один ход')
                continue

        elif pc_field[coord1][coord2] == ' ':  # если клетка пуста, то выводится промах
            pc_field[coord1][coord2] = '.'
            print('Промах')
        elif pc_field[coord1][coord2] == ('.' or 'X'):
            print('Клетка занята, выберите другую клетку')
            continue


        #ход пк

        while True:
            # Для выбора клетки стрельбы, ПК, будет создавать массив списков с индексами клеток в которых нет промахов
            # или попаданий по кораблям из поля game_field (поля с кораблями игрока)
            # выбор координаты по строке, случацным образом
            coord_pc = (field_player_for_pc(game_field))
            # выбор колонки из строки
            coord_pc_1 = random.randint(0, len(coord_pc)-1)
            if len(coord_pc[coord_pc_1]) == 0:  # проверка на не пустоту списка
                continue
            coord_pc_2 = random.choice(coord_pc[coord_pc_1])
            coord_pc_1 += 1

            if player_field[coord_pc_1][coord_pc_2] == '■':  # проверка попадания по кораблю
                player_field[coord_pc_1][coord_pc_2] = 'X'  # если попадание есть, то меняем ■ на Х
            # если функция проверки наличия в округе кораблей показывает их отсутсвие, то переходим в функцию
            # отрисовки ореола потопленного корабля
                if check_buoyancy_ship(pc_field, coord1, coord2):
                    print('потоплен ваш корабль')
                    halo_ship(player_field, coord_pc_1, coord_pc_2)
                    if check_ship(player_field):
                        print('Игра окончена')
                        break
                    continue
                else:
                    print('попадание по вашему кораблю')
                    continue

            elif player_field[coord_pc_1][coord_pc_2] == ' ':  # если клетка пуста, то выводится промах
                player_field[coord_pc_1][coord_pc_2] = '.'
                print('промах пк')

            break


while True:
    answer = input('Чтобы начать новую игру нажмите "enter": ')
    game()

