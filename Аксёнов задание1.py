def calculate(n):
    def product(j):
        if j == 1:
            return 1 - 1 / (1 ** 2)
        return ( 1-1 / (j ** 2)) * product(j - 1)
    def summ(k):
        if k == 1:
            return product(1)
        return product(k) + summ(k - 1)
    return summ(n)


n = int(input("Введите n:"))
print("s="calculate(n))