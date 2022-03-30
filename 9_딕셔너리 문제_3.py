# 딕셔너리 리스트를 이용해 유저정보를 출력해주세요.
user1 = {"아이디" : "hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디" : "sony7"  , "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디" : "ryu99"  , "비밀번호" : "9999", "이름" : "류현진"}

user_list = [user1, user2, user3]

# 아이디를 넘기면 그 아이디에 해당하는 회원 딕셔너리 얻어오기
def get_user_by_id(id) :
    for user in user_list :
        if user["아이디"] == id :
            return user

def print_all_userid() :
    for user in user_list :
        print(user["아이디"])    

# 모든 회원 아이디를 출력
print("===================================")
print("모든 회원 아이디 출력")
print_all_userid()

# 출력 :
'''
hong123
sony7
ryu99
'''

        
print("===================================")
# hong123 아이디를 가진 회원의 이름 출력
# 출력 : 홍길동

user1 = get_user_by_id("hong123")
print(user1["이름"])
print(user1["비밀번호"])
print("===================================")        

# hong123 아이디를 가진 회원의 비밀번호를 3333으로 수정 후 모든 회원 정보 출력
# 출력 : 홍길동의 비밀번호가 3333으로 수정되어 출력되어야 함
print("hong123 유저 비밀번호 3333으로 수정")
user2 = get_user_by_id("hong123")
user2["비밀번호"] = 3333
print(user1["비밀번호"])
print("===================================")
# 아이디가 chacha, 이름 김지상, 비밀번호 c123인 회원을 추가
print("김지상 회원 추가")
cha = {"아이디" : "chacha", "이름" : "김지상", "비밀번호" : "c123"}
user_list.append(cha)

print("===================================")
print("회원 목록 확인")
print_all_userid() # 회원 확인
print("===================================")

# 아이디가 hong123, 이름 홍길순, 비밀번호 h1234 인 회원추가
# 아이디가 중복될 시 추가 거부.
hong = {"아이디" : "hong123", "이름" : "홍길순", "비밀번호" : "h1234"}
user = get_user_by_id(hong["아이디"]) # 함수는 리턴값이 없을 때 None
print("===================================")
print("홍길순 회원 추가")
# 이미 존재하는 회원이면 해당 회원의 딕셔너리가 리턴, 아니면 None 리턴
if user != None :
    print("이미 존재하는 회원입니다.")
else :
    user_list.append(hong)

print("===================================")
print("회원 목록 확인")
print_all_userid() # 회원 확인
print("===================================")
