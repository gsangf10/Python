# n과 m 사이의 수 중 k의 배수 출력

n = 10
m = 30
k = 3
while n <= m:
  if n % k == 0:
    print(n, end=" ")
  n += 1
