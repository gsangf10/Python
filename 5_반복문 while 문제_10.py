# 구구단 2~9단 출력해주세요.

n = 2
while n <= 9:
  print("== {} 단 ==".format(n))
  m = 1
  while m <= 9:
    print("{} * {} = {}".format(n,m,n*m))
    m += 1
  n += 1
