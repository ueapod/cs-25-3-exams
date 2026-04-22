def product(k, j=1, acc=1):
    if j > k:
        return acc
    return product(k, j + 1, acc * j)

def sumS(n, k=1, acc=0):
    if k > n:
        return acc
    return sumS(n, k + 1, acc + product(k))

n = int(input())

print(sumS(n))