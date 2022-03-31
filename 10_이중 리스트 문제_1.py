# list1 리스트만 이용해서 아래와 같이 출력해주세요.

list1 = [[1,2,3], [4,5,6], [7,8,9]]

'''
1 4 7 
2 5 8
3 6 9
'''
for i in range(len(list1)) :
  for j in range(len(list1[i])) :
    print(list1[j][i], end=" ")
  print()

print("=====")
'''
3 4 9 
2 5 8
1 6 7
'''
e_idx = len(list1) - 1
o_idx = 0
for i in range(len(list1)) :
  for j in range(len(list1[i])) :
    if j % 2 == 1 :
      print(list1[j][o_idx], end=" ")
    else :
      print(list1[j][e_idx], end=" ")
  print()
  o_idx += 1
  e_idx -= 1
