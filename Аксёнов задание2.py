s = int(input("Введите строку: "))
count = {}
for char in s:
    count[char] = count.get(char, 0) + 1
max_char = None
max_count = 0
for char, c in count.items():
    if c > max_count:
        max_count = c
        max_char = char
print("Самый частый символ:", max_char)
print("Количество вхождений:", max_count)