import random
SIZE = 7
M = list(range(SIZE))


def get_next_fitting_member(matrix, x, y, elements=list(range(SIZE + 1))):
    print("get_next_fitting_member x:" + str(x) + " y:" + str(y))
    for i in range(x):
        if matrix[i][y] in elements:
            elements.remove(matrix[i][y])
    for i in range(y):
        if matrix[x][i] in elements:
            elements.remove(matrix[x][i])
    if (len(elements) > 1):
        print(elements)
        matrix[x][y] = elements[0]
    else:
        newElements = list(range(SIZE+1))
        back = random.randint(1, x-1)
        newElements.remove(matrix[x-back][y])
        print("newElements: " + str(newElements))
        get_next_fitting_member(matrix, x-back, y, newElements)
        for i in range(back):
            get_next_fitting_member(matrix, x-back+i, y)


def print_matrix(matrix):
    for y in M:
        s = ""
        for x in range(SIZE):
            s += str(matrix[x][y]) + " "
        print(s)


matrix = [[0] * SIZE for i in range(SIZE)]

for y in range(SIZE):
    for x in range(SIZE):
        if x == 0:
            matrix[x][y] = y
        elif y == 0:
            matrix[x][y] = x
        else:
            get_next_fitting_member(matrix, x, y)

print_matrix(matrix)
