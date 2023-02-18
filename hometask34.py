# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:                                         Вывод:
# print_operation_table(lambda x, y: x * y)     1   2   3   4   5   6
#                                               2   4   6   8   10  12
#                                               3   6   9   12  15  18
#                                               4   8   12  16  20  24
#                                               5   10  15  20  25  30
#                                               6   12  18  24  30  36
# 1. функция создает матрицу, принимает количество строк и столбцов, возвращает список
def create_matrix(row, column):
    matrix = [[0] * column for i in range(row)]
    return matrix


# 2. функция распечатывает матрицу в виде таблицы( принимает матрицу в виде списка)
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


# принимает кол строк, возвращает матрицу в виде списка (заполнение с консоли)
def matrix_from_console(rows):
    a = []
    for i in range(rows):
        a.append([int(j) for j in input('numbers in row: ').split()])
    return a


# функция которая принимает лябда выражение и по нему выводит значение индекса внутри матрицы
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print("%4d" % operation(j, i), end=' ')  # для красивого вывода
        print()


print_operation_table(lambda x, y: x - y, 5, 7)

