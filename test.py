# TODO Что выведет программа в результате выполнения кода?

A = [3, 5, 8, 2, 1, 4, 3, 1, 2, 6]
s = 0
for i in range(0, 9):
    if A[i] < A[9]:
        t = A[i]
        A[i] = A[8 - i]
        A[8 - i] = t
        s = s + t
print(s)
print(A)