# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.

age = 33

# if만 사용
if age <= 19 :
  print("할인 대상이 아닙니다.")
if age >= 60 :
  print("할인 대상이 아닙니다.")
if age > 20 :
  if age < 60 :
    print("할인 대상입니다.")

# elif, else 사용
if age < 20:
  print("할인 대상입니다.")
elif age > 59 :
  print("할인 대상입니다.")
else :
  print("할인 대상이 아닙니다.")
