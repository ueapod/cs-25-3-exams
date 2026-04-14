string = str(input("строка: "))
string2 = str()
for i in range(len(string)):
    for j in range(len(string)):
        if string[i] == string[j]:
            break
        if j == len(string):
            string2 += string[i]
print(string2)