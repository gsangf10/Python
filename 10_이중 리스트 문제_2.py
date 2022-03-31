arr = [1,5,2,6,3,7,4];
rst = []
# cmd에 3개의 리스트. 각 리스트의 원소를 i, j, k라고 할 때,
cmd = [[2,5,3], [4,4,1], [1,7,3]];

# arr 리스트의 i번째부터 j번째까지 자른 후 k번째의 값을 새로운 리스트에 담아서 출력
# 예를 들어 cmd의 첫번째 리스트는 i가 2, j가 5, k가 3이므로
# arr의 2번째 값에서 5번째값까지 [5,2,6,3]으로 잘라진다.
# [5,2,6,3] 에서 k가 3으로 3번째 값을 뽑으면 6이 나온다.
# 이와 같은 방식으로 cmd의 세 리스트에 맞게 값을 뽑아주면 된다.


# version1
m = 0

while m < 3 :
  
  i = cmd[m][0]
  j = cmd[m][1]
  k = cmd[m][2]

  tmp = []

  n = i - 1
  while n < j :
    tmp.append(arr[n])
    n += 1
  
  rst.append(tmp[k-1])

  m += 1

print(rst)

# 출력 : 6, 6, 2


# version2
m = 0

while m < 3 :
  
  i = cmd[m][0]
  j = cmd[m][1]
  k = cmd[m][2]

  rst.append(arr[i - 1 : j][k-1])

  m += 1

print(rst)
