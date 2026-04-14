string = str(input("строка: "))
string2 = str()
for i in string:
    if i not in string2:
        string2 +=i
print(string2)
