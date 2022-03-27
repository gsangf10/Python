list1 = [1, 11, 43, 23, 56, 89, 101, 111, 120]
list2 = [2, 5, 7, 10, 11, 14, 19, 22, 33]

# get_even_list 함수를 완성시켜주세요.
def get_even_list(param_list) :
    result = [] # 짝수만 담을 리스트
    for num in param_list :
        if num % 2 == 0 :
            result.append(num)  
    
    return result

rst1 = get_even_list(list1)
print(rst1) # 출력 : [56, 120]

rst2 = get_even_list(list2)
print(rst2) # 출력 : [2, 10, 14, 22]
