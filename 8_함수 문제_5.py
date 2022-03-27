list1 = [2,4,8,12,44,56,151,445,600]
list2 = [12,34,552,45,123,68,29,554]

# list1의 모든 요소의 평균과 list2의 모든 요소의 평균을 구해서 두 수의 합을 구하시오. (내장함수 사용 X)
def get_avg_of_list(param_list) :
    sum1 = 0
    for num in param_list :
        sum1 += num

    return (sum1 / len(param_list))


rst = get_avg_of_list(list1) + get_avg_of_list(list2)
print(rst)
