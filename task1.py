s = input()
 
result = " " 
seen = " "

for c in s:
	if c not in seen:
		result += c 
		seen += c
print(result)  