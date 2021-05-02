# ID="flower"
# password="1234"

# 아이디와 비밀번호를 입력 받아서
# 등록된 아이디와 비밀번호 비교하여 '로그인 성공' 또는 '로그인 실패' 출력

# 아이디 입력: abcd (입력)
# 비밀번호 입력: 1234
# 로그인 실패
# 
# 아이디 입력: flower (입력)
# 비밀번호 입력: 1234
# 로그인 성공

ID="flower"
password="1234"
input_id = input("아이디 입력: ")
input_pass = input("비밀번호 입력: ")

if ID != input_id or password != input_pass:
    print("로그인 실패")
else:
    print("로그인 성공")