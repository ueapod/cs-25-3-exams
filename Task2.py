def Sum(n):
    if n == 0:
        return 0
    def multy(n):
        if n == 0:
            return 1
        return n/(n + 2) + multy(n - 1)
    return multy(n) + Sum( n - 1)
n = int(input())
example = Sum(n)
print(example)
    
