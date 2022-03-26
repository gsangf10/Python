# for문 개념

# while 문과 같은 반복문이다.

# for문의 기본 구성
# for 변수 in range(반복횟수):
# => range 안의 숫자는 0 부터 시작하여 해당 숫자 전 까지 실행된다.

# 출력 0 1 2 3 4
for i in range(5): # range(5)는 0부터 4까지
  print(i)

# for 변수 in range(처음 숫자, 마지막 숫자, 증감값):
# => 처음숫자 부터 시작하여 마지막 숫자 -1 까지 증감값을 가지고 실행된다.
# => 증감값은 생략 가능하다.

# 출력 2 4 6 8
for i in range(2,10,2): # 2 부터 9 까지 2 증가
  print(i)


# for 변수 in 리스트: 로 사용하면 리스트 인덱스를 순차적으로 반환한다.

a_list = [4,2,5,2,3,4,7]

# 출력 4 2 5 2 3 4 7
for a in a_list:
  print(a)


# for 변수1, 변수2 in enumerate(리스트): 로 사용하면 변수1, 변수2에 각각 인덱스 번호와 값을 반환한다.

a_list = [4,2,5,2,3,4,7]
for a, b in enumerate(a_list): # a = 인덱스 번호, b = 리스트의 값
  print(a, b)
