# 개념

# 명령어 == 코드 == 코드를 적어놓은 파일 == 소스코드 파일
# 여러 명령어(코드)를 작성 -> 소스코드 -> 소스코드 4가지 뼈대
# 자료, 변수, 조건문, 반복문

# 흐름제어
# 실행이 될 때도 있고 안될 때도 있고 -> 조건문

print("1")

# if 다음 True가 오면 indent된 코드를 실행.
# if 다음 False가 오면 indent된 코드를 건너 뜀.
if False :
    print("2") # indent, 들여쓰기

print("3")


# 날씨 변수
weather = "맑음"

# 비가 오면 창문을 닫아라
if weather == "비":
    print("창문을 닫다")

# 비가 오지 않으면 창문을 열어라    
if weather != "비" :
    print("창문을 열다")

# 소지금
money = 10000

# 소지금이 2만원 이상이면 치킨을 먹고
# 소지금이 2만원 미만이면 떡볶이 먹기.

# 동전을 던질 때 앞면이 나옴.
# 당신은 남자입니까? 아니요 -> 여자임

# if else 문 -> 둘 중 하나를 선택할 때.
if money >= 20000 :
    print("치킨을")    
    print("먹는다")

else :
    print("떡복이를")
    print("먹는다")
    
sex = "여자"

if sex == "남자" :
    print("남자입니다.")
    
else :
    print("여자입니다.")

# 비슷한 예제
# 동전 앞뒤
# 할인대상여부
# 짝수 홀수
