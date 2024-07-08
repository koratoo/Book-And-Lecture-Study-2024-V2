# 똑같은 값을 여러 번 구한다면, 배열에 저장하여 재사용하는 것이 좋다.

def fibo(x):
	global arr

	if arr[x] != -1:
		return arr[x]

	arr[x] = fibo(x - 1) + fibo(x - 2)
	return arr[x]


n = int(input())

arr = [-1] * (n + 2)
arr[0] = 0
arr[1] = 1

print(fibo(n))