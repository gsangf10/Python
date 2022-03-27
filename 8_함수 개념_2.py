# 함수 리턴 개념

# 원의 넓이를 구하기.
# 반지름 X 반지름 X 3.14(원주율)


def circle_area(r) :
    return r * r * 3.14

# 반지름이 5인 원의 넓이
circle_area(5)

# 반지름이 10인 원의 넓이
circle_area(10)

# 반지름 3인 원의 넓이
circle_area(3)

# 반지름이 4인 원의 넓이에다가 2배
print( circle_area(4) * 2 ) 

# 반지름이 5인 원의 넓이의 절반
print( circle_area(5) / 2 )

# 함수가 값을 리턴하지 않으면 None이 되기 때문에 계산이 안된다. 여기서 None은 값이 없음의 의미한다.
# 리턴(반환) -> 함수의 결과값을 받아서 2차 작업을 하기 위해 함수가 값을 내보는 것.(함수가 값으로 바뀌는 것으로 이해해도 좋다)

# 자판기 함수
def vending_machine(input_money, no) :
    
    print("현재 투입 금액 : {}원".format(input_money))
    
    beverages = ["사이다", "콜라", "커피", "생수"]
    prices = [1000, 1200, 800, 700]
    
    if prices[no] > input_money :
        print("잔액이 부족합니다.")
        return
    
    print("잔액은 {}원".format(input_money - prices[no]))
    
    return beverages[no]


# 0. 사이다,  1. 콜라,  2. 커피,   3. 생수
result = vending_machine(1000, 3)
