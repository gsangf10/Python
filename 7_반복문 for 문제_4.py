# 구구단은 n단 ~ m단 중 홀수단만 1 ~ limit 까지 곱 중 짝수곱만 출력해주세요.

n = 4;
m = 19;
limit = 11;

'''  출력 예시

5 * 2 = 10
5 * 4 = 20
5 * 6 = 30
5 * 8 = 40
5 * 10 = 50

7 * 2 = 14
7 * 4 = 28
7 * 6 = 42
7 * 8 = 56
7 * 10 = 70
...
...
19 * 2 = 38
19 * 4 = 76

'''

# while 버전
dan = n
while dan <= m :

  i = 1
  if dan % 2 != 0 :
    while i <= limit :
      if i % 2 == 0 :
        print("{} * {} = {}".format(dan, i, dan*i))
      i = i + 1

  dan = dan + 1

# for 버전
for dan in range(n, m + 1) :
  if dan % 2 != 0 :
    for gob in range(1, limit+1) :
      if gob % 2 == 0 :
        print("{} * {} = {}".format(dan, gob, dan*gob))
