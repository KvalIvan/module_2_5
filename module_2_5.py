def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Сколько строк должно быть в матрице : '))
m = int(input('Сколько столбцов должно быть в матрице : '))
value = input('Дайте значение матрицы : ')
print('-------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print("Невозможное кол-во строк:", n)
elif m <= 0:
    print("Невозможное кол-во столбцов:", m)
