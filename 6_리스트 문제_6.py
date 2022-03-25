# n부터 m까지의 수중 3의 배수이거나 7의 배수인 수들의 합 구하기

# 이 값들을 바꿔가면서 실행해주세요
n = 2
m = 10


# n ~ m 까지 출력
i = n
while i <= m:
  print(i, end=' ')
  i += 1
print()

# n ~ m 까지 3의 배수만 출력
i = n
while i <= m:
  if i % 3 == 0:
    print(i, end=' ')
  i += 1
print()

# n ~ m 까지 3의 배수이거나 7의 배수인 수 출력
i = n
while i <= m:
  if i % 3 == 0 or i % 7 == 0:
    print(i, end=' ')
  i += 1
print()

# n ~ m 까지 3의 배수이거나 7의 배수인 수의 합 출력
i = n
s = 0
while i <= m:
  if i % 3 == 0 or i % 7 == 0:
    s += i
  i += 1
print(s)
