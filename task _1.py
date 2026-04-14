#1 variant
#task 1
a = 'Привет как дела'
a.split(' ')
print(len(a))
for i in range(len(a)):
    b,c = a[i - 1] , a[i]
    if len(b) >= len(c):
        print(b)
    else:
        print(c)
