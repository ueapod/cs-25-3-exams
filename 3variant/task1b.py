string = str(input("строка: ")) #работает
string2 = str()
for i in range(len(string)):
    if string[i] not in string2:
        string2 += string[i]
print(string2)
