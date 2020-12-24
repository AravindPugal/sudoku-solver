import numpy as np
question = np.array([
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
])
solution = np.copy(question)
previous_memory = np.ones((9, 9), dtype=int)
i, j = 0, 0
is_back = 0

# this method will find what are the elements in row column squrebox


def barrier(row, col):
    squre_arr = []
    column_arr = []
    row_arr = []

    # it will find 3*3 array related to element position
    squre_box_finder = [(0, 3), (0, 3), (0, 3),
                        (3, 6), (3, 6), (3, 6),
                        (6, 9), (6, 9), (6, 9)]
    row_start, row_end = squre_box_finder[row]
    col_start, col_end = squre_box_finder[col]
    while row_start < row_end:
        while col_start < col_end:
            element = solution[row_start][col_start]
            if element != 0:
                squre_arr.append(element)
                col_start += 1
            else:
                col_start += 1
        row_start += 1
        col_start = col_end-3
    # end of squre array finder

    # row and column arr finder
    for i in range(9):
        element1 = solution[row][i]
        element2 = solution[i][col]
        if element1 != 0 and element2 != 0:
            row_arr.append(element1)
            column_arr.append(element2)
        elif element1 != 0:
            row_arr.append(element1)
        elif element2 != 0:
            column_arr.append(element2)
        else:
            pass
    return row_arr, column_arr, squre_arr
    # end of row and column array finder


while i < 9:
    while j < 9:
        if not question[i][j]:  # to check the position already filled or not
            row, col, squre = barrier(i, j)
            possible_number = previous_memory[i][j]
            while possible in row or possible in col or possible in squre:
                possible_number += 1
            if possible < 10:
                solution[i][j] = possible_number
                previous_memory[i][j] = possible_number
                is_back = 0
                j += 1
            else:
                solution[i][j] = 0
                possibility[i][j] = 1
                is_back = 1
                if j > 0:
                    j -= 1
                else:
                    j = 8
                    i -= 1
        else:
            if is_back:
                if j > 0:
                    j -= 1
                else:
                    j = 8
                    i -= 1
            else:
                j += 1
    i += 1
    j = 0
print(solution)

# qus
# [
#     [0, 0, 0, 2, 6, 0, 7, 0, 1],
#     [6, 8, 0, 0, 7, 0, 0, 9, 0],
#     [1, 9, 0, 0, 0, 4, 5, 0, 0],
#     [8, 2, 0, 1, 0, 0, 0, 4, 0],
#     [0, 0, 4, 6, 0, 2, 9, 0, 0],
#     [0, 5, 0, 0, 0, 3, 0, 2, 8],
#     [0, 0, 9, 3, 0, 0, 0, 7, 4],
#     [0, 4, 0, 0, 5, 0, 0, 3, 6],
#     [7, 0, 3, 0, 1, 8, 0, 0, 0],
# ]
