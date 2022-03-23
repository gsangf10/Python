# 1 ~ 500 사이의 수 중 4의 배수만 출력

n = 1
while n <= 500:
  if n % 4 == 0:
    print(n, end=" ")
  n += 1
