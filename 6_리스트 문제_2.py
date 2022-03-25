#  1 ~ 10 까지 수 리스트 선언 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [i for i in range(1,11)]


# 리스트 값 짝수만 가져오기
i = 0
while i < len(list1):
  if list1[i] % 2 == 0:
    print(list1[i], end=' ')
  i += 1
print()

# 리스트에 11, 13, 15 추가하기
list1.extend([11, 13, 15])
print(list1)


# 리스트의 짝수번째 값 1증가시키기
i = 1
while i < len(list1):
  list1[i] += 1
  print(list1[i], end=' ')
  i += 2
print()


# 리스트에서 세번째 값 지우기
del list1[2]
print(list1)
