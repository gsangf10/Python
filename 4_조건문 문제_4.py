'''
어떤 차의 높이가 170cm 입니다..

이 차는 3개의 터널을 차례대로 지나게 될 것입니다.

터널의 높이가 차의 높이보다 같거나 낮다면 차는 터널과 충돌하여 사고가 납니다.

터널의 높이가 차례대로 3개 주어지고 터널을 무사히 잘 통과하면 PASS 를 출력하고, 사고가 난다면 CRASH 를 출력하세요.

예시 ) tunel1 = 162
       tunel2 = 180
       tunel3 = 166

터널의 높이가 위와 같다면 tunel1과 tunel3에서 걸리므로 CRASH
'''

tunel1 = 179
tunel2 = 185
tunel3 = 163

if tunel1 < 170 :
  print("CRASH")
elif tunel2 < 170 :
  print("CRASH")
elif tunel3 < 170 :
  print("CRASH")
else :
  print("PASS")
