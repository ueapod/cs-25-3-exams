# 1 Задание 
a = input()
b = input()

if len(a) != len(b):
    print("Не анаграммы")
else:
    count = {}

    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in b:
        if i in count:
            count[i] -= 1
        else:
            print("Не анаграммы")
            break
    else:
        print("Анаграммы")




# 2 Задание 
import math

def product(k, j=1):
    if j > k:
        return 1
    return (j / math.factorial(j + 1)) * product(k, j + 1)

def S(n, k=1):
    if k > n:
        return 0
    return product(k) + S(n, k + 1)

n = int(input("Введите n: "))
print("S =", S(n))