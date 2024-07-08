# 똑같은 값을 여러 번 구한다면, 배열에 저장하여 재사용하는 것이 좋다.
# 재귀함수 + 중복계산 메모이제이션을 사용한다.
# 몇 백만번 연산 -> 몇 십번 연산으로 바뀐다.
# 값을 -1로 초기화 -> 값이 채워지지 않은 대상만 fib(x-1) + fib(x-2) 연산
def fibo(x):
	global arr

	if arr[x] != -1:
		return arr[x]

	arr[x] = fibo(x - 1) + fibo(x - 2)
	return arr[x] # 계산한 값을 저장한다는 개념 


n = int(input())

arr = [-1] * (n + 2)
arr[0] = 0
arr[1] = 1

print(fibo(n))