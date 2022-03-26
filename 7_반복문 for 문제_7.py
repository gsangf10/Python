# for문을 이용해 list이용하기
list1 = [1,2,3,4,5,6,7,8,9,10]

# 1. 위 리스트를 for문을 이용해 출력해주세요.

print("=========1. while ===========")
a = 0

while a < len(list1) :
  print(list1[a])
  a += 1

print("=========1. for .. in ===========")
for v in list1 :
  print(v)

print("=========1. range() ===========")
for i in range(len(list1)) :
  print(list1[i])  

# 2. 위 리스트를 for문을 이용해 3의 배수만 출력해주세요.

print("=========2. while ===========")
a = 0

while a < len(list1) :
  if list1[a] % 3 == 0 :
    print(list1[a])
  a += 1
  
print("=========2. for .. in ===========")
for v in list1 :
  if v % 3 == 0 :
    print(v)

print("=========2. range() ===========")
for i in range(len(list1)) :
  if list1[i] % 3 == 0 :
    print(list1[i])
# 3. 위 리스트를 for문을 이용해 리스트의 모든 값들을 더한 값을 출력해주세요.

print("=========3. while ===========")
a = 0
total = 0
while a < len(list1) :
  total += list1[a]
  a += 1
print(total)

print("=========3. for .. in ===========")
total = 0
for v in list1 :
  total += v
print(total)


print("=========3. range() ===========")
total = 0
for i in range(len(list1)) :
  total += list1[i]
print(total)
