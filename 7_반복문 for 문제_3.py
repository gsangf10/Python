# n부터 m까지의 수중 3의 배수이거나 7의 배수인 수들의 합 구하기

# 이 값들을 바꿔가면서 실행해주세요
n = 12
m = 100


# while
result = 0
num = n

while num <= m :
  if num % 3 == 0 or num % 7 == 0 :
    result += num
  num += 1

print(result)

# for
result = 0
for num in range(n, m + 1) :
  if num % 3 == 0 or num % 7 == 0 :
    result += num

print(result)
