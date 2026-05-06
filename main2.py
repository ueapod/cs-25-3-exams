# 1
s = input("Введите строку: ")

words = s.split()

longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print("Самое длинное слово:", longest)
print("Длина слова:", len(longest)) 

# 2
def summa(j):
    if j == 1:
        return (-1) / (1**2)
    else:
        return summa(j - 1) + ((-1)**j) / (j**2)


def P(k):
    if k == 1:
        return summa(1)
    else:
        return P(k - 1) * summa(k)


n = int(input("Введите n: "))
print("P =", P(n))