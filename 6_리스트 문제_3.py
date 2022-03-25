list1 = [2,5,9,11,23,51,26,38,41,93,101]

# 위 리스트의 모든 값을 출력해주세요.
# 출력 : 2, 5, 9, 11, 23, 51, 26, 38, 41, 93, 101
print(list1)

# 위 리스트의 '홀수번째 인덱스' 값만 출력해주세요.
# 출력 : 5, 11, 51, 38, 93
i = 1
while i < len(list1):
  print(list1[i], end=' ')
  i += 2
print()

# 위 리스트의 '짝수값'만 출력해주세요. 
# 출력 : 2, 26, 38
i = 0
while i < len(list1):
  if list1[i] % 2 == 0:
    print(list1[i], end=' ')
  i += 1
print()

# 위 리스트의 값으로 구구단을 만들어주세요
# 출력 : 2단, 5단, 9단, 11단, 23단, 51단, 26단, 38단, 41단, 93단, 101단
i = 0
while i < len(list1):
  j = 1
  print("=== {} 단 ===".format(list1[i]))
  while j <= 9:
    print("{} * {} = {}".format(list1[i], j, list1[i] * j))
    j += 1
  i += 1

# 위 리스트의 값을 거꾸로 출력해주세요.
# 출력 : 101, 93, 41, 38, 26, 51, 23, 11, 9, 5, 2
i = len(list1) - 1
while i >= 0:
  print(list1[i], end=' ')
  i -= 1
print()
