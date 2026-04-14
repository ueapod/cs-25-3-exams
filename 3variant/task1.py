string = str(input("строка: "))
i=0
j=0
while i < len(string):
    while j < len(string):
        if string[i] == string[j]:
            string = string[:j] + string[j+1:]
            j -= 1
        j += 1
    i += 1
print(string)