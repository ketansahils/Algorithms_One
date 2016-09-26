import math

def test(n):
	arr = [k for k in range(n)]
	n = len(arr)
	i = 2
	while i <= math.sqrt(n):
		if arr[i]:
			j = i
			while i+j < n:
				arr[i+j] = False
				j = j + i
		i = i + 1
	return arr


print [k for k in test(100) if k]