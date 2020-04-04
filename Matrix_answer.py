import numpy as np

num_of_rows = int(input('Enter number of rows.'))
mat = []
for i in range(num_of_rows):
    print(f"enter row number {i + 1}")
    mat.append(list(map(float, input().split())))
answers = np.zeros((num_of_rows, 1))
for i in range(num_of_rows):
    print(f'Enter answer number {i + 1}')
    answers[i] = float(input())
mat = np.hstack((mat, answers))
print("your augmented matrix is : ")
print(mat)


def change_row_num(a_mat, first, second):
    print("enter change_row_num")
    temp = np.copy(a_mat[first])
    a_mat[first] = a_mat[second]
    a_mat[second] = temp
    print(f"changin {first} and {second}")
    print(a_mat)
    return a_mat


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
print("calculating rref")

for i, j in pivot_dict.items():
    if i:
        for k in range(1, i + 1):
            mat = multiple_rows(mat, i - k, i, mat[i - k][j] * -1)
print(mat)
x = 0
ans_dict = {}
inconsistent = False
for i in range(num_of_rows):
    if np.count_nonzero(mat[i])==1:
        if mat[i][mat.shape[1]-1]:
            inconsistent = True
            print(f"0 = {mat[i][mat.shape[1]-1]}")
    elif np.count_nonzero(mat[i]):
        pivot = pivot_dict[i]
        print(f'x{pivot + 1} =', end=" ")
        for j in range(pivot + 1, mat.shape[1] - 1):
            if mat[i][j]:
                print(f'-{mat[i][j]}x{j + 1}', end=" ")
        print(f"+{round(mat[i][mat.shape[1] - 1],2)}")
if inconsistent:
    print("this is inconsistent and doesn't have any answer!")

