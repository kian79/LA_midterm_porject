import numpy as np
num_of_rows = int(input('Enter number of rows.'))
mat = []
for i in range(num_of_rows):
    print(f"enter row number {i + 1}")
    mat.append(list(map(float, input().split())))
mat = np.array(mat)
print(mat)

def change_row_num(a_mat, first, second):
    print("enter change_row_num")
    temp = np.copy(a_mat[first])
    a_mat[first] = a_mat[second]
    a_mat[second] = temp
    print(f"changin {first} and {second}")
    print(a_mat)
    return a_matx


def multiple_row(a_mat, row_num, num):
    print("enter multiple_row")
    a_mat[row_num] = list(map(lambda x: x * num, a_mat[row_num]))
    print(f"multipling {row_num} in {num}")
    print(a_mat)
    return a_mat


def multiple_rows(a_mat, first, second, num):
    print("entering multiple_rows")
    for i in range(len(a_mat[first])):
        a_mat[first, i] = a_mat[second, i] * num + a_mat[first, i]
    print(f'multipling {second} and {num} and adding to {first}')
    print(a_mat)
    return a_mat


pivot_dict = {}
for i in range(num_of_rows):
    for j in range(i, mat.shape[1]):
        flag = False
        if not mat[i][j]:
            for k in range(1, num_of_rows - i):
                if mat[i + k][j]:
                    mat = change_row_num(mat, i, i + k)
                    flag = True
                    break
            if not flag:
                continue
        mat = multiple_row(mat, i, 1 / mat[i][j])
        pivot_dict[i] = j
        if i != num_of_rows - 1:
            for k in range(1, num_of_rows - i):
                mat = multiple_rows(mat, i + k, i, mat[i + k][j] * -1)
        break
print(mat)

rank = 0
for i in range(num_of_rows):
    if np.count_nonzero(mat[i]):
        rank+=1
print(" rank : ",rank)
print("dim null : ", mat.shape[1]-rank)