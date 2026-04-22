#4 variant
#task 2
def sum(n):
    if n == 0:
        return 0
    def mult(n):
        if n == 0:
            return 1
        return (-1)**n+1/n * mult(n-1)
    return mult(n) + sum(n-1)
n = int(input())
result = sum(n)
print(result)
