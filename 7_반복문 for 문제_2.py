# 999단을 출력해주세요.
"""
1 * 1 * 1 = 1
1 * 1 * 2 = 2
1 * 1 * 9 = 9
1 * 2 * 1 = 2
1 * 2 * 2 = 4
....
2 * 1 *  1 = 2
....
....
....
9 * 9 * 8 = 648
9 * 9 * 9 = 729
"""

# while 버전
i = 1
while i < 10 :
  j = 1
  while j < 10 :
    k = 1 
    while k < 10 :
      print("{} * {} * {} = {}".format(i, j, k, i * j * k))
      k += 1    
    j += 1  
  i += 1

# for 버전
for i in range(1, 10) :
  for j in range(1, 10) :
    for k in range(1, 10) :
      print("{} * {} * {} = {}".format(i, j, k, i * j * k))
