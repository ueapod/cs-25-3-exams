s = input()
sub = input()

n = len(s)
m = len(sub)

pos = -1

i = 0
while i <= n - m:
    j = 0
    ok = True

    while j < m:
        if s[i + j] != sub[j]:
            ok = False
            break
        j += 1

    if ok == True:
        pos = i
        break

    i += 1

print(pos)