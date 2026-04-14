def product(j):
	if j==1:
		return 1-1/(1**2)
	return product(j-1) * (1-1/(j**2))

def sum_s(k):
	if k == 1:
	return product(1)
	return sum_s(k-1) + product(k)
n = int(input(" "))
S = sum_s(n)

print (" ", s)