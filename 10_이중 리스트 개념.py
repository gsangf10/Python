# 이중리스트 개념

list1 = [[1]] # 이중리스트
list2 = [1] # 일중리스트

'''
1 2 3
4 5 6
7 8 9
'''

list3 = [1,2,3]
list4 = [4,5,6]
list5 = [7,8,9]

list6 = [list3, list4, list5] 

# 이중리스트는 보통 행렬을 표현할 때 많이 사용
print(list6)

# 2행 1열 값 꺼내기
print(list6[0]) # 1행
print(list6[1]) # 2행
print(list6[2]) # 3행

list7 = list6[1] # 2행을 list7 변수에 담는다.
print(list7[0]) # list7의 첫번째 값 ==> 2행 1열

print(list6[1][0]) # list[행][열]


# 이중리스트 전체 탐색
# 첫번째행 잡고 모든 열 탐색
# 두번째행 잡고 모든 열 탐색
# 세번째행 잡고 모든 열 탐색

# 행렬 전체 탐색

list3 = [1,2,3]
list4 = [4,5,6]
list5 = [7,8,9]

list6 = [list3, list4, list5]
list7 = [[1,2,3], [4,5,6], [7,8,9]]

'''

1 2 3
4 5 6
7 8 9

'''

for row in list7 :
    for col in row :
        print(col, end=" ")
    print()
    
for i in range(0, 3, 1) :
    row = list7[i]
    for j in range(0, 3, 1) :
        print(row[j], end=" ")
    print()
