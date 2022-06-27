def start():
    print('Игра Крестики-нолики')
    print('Формат ввода: (строка) (столбец)')
    print('')

start()

field_list = [["-"] * 3 for i in range(3) ]

def field(field_list):
    print('  0 1 2')
    for i in range(3):
        print(f'{i} {field_list[i][0]} {field_list[i][1]} {field_list[i][2]}')
    print()

field(field_list)

def step_x():
    while True:
        mark = input('Введите ваш ход: ').split()
        if len(mark) != 2:
            print('Данные введены некорректно')
            continue
        x, y = mark
        if not x.isdigit() or not y.isdigit():
            print('Введите числа')
            continue
        x, y = int(x), int(y)
        if 0>x or x>2 or 0>y or y>2:
            print('Неверный диапазон')
            continue

        if field_list[x][y] != '-':
            print('Клетка занята')
            continue
        return x, y

def check(field_list=[[0,0],[0,0]]):
    coords = (((0,0), (0,1), (0,2)), ((1,0),(1,1),(1,2)), ((2,0), (2,1), (2,2)),
              ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)),((0,2), (1,2), (2,2)),
               ((0,0), (1,1), (2,2)),((0,2), (1,1), (2,0)))
    for coord in coords:
        check_counter = ''
        for c in coord:
            check_counter += field_list[c[0]][c[1]]
        if check_counter == 'xxx':
            print('XXX!')
            return True
        if check_counter == 'ooo':
            print('OOO!')
            return True

count = 0
while True:
    count += 1
    if count % 2 == 1:
        print('Ходят Х')
        x, y = step_x()
        field_list[x][y] = 'x'
        field(field_list)

    if count % 2 == 0:
        print('Ходят О')
        x, y = step_x()
        field_list[x][y] = 'o'
        field(field_list)
    if check(field_list):
        break
    if count == 9:
        print('Ничья')
        break