# 이메일 주소를 입력 받아서, 이메일 형식이 아니면
# "이메일 형식이 아닙니다"출력하기
# 이메일 입력: ab.com
# 이메일 형식이 아닙니다.
# 입력한 이메일: ab.com

# 이메일 형식이 아닌 경우
# - @ 없는 경우
# - . 이 없는 경우

email = input("이메일 입력: ")
if(email.find("@")==-1 or
    email.find(".") == -1 or
     email.find("@") > email.find(".") or
      email.find(".") - email.find("@") <2 or
      email.find("@")==0 or
      len(email) - email.find(".") <= 1 or
      email.count("@") >= 2 or
      email.count(".") >=2 ):
    print("이메일 형식이 아닙니다.")
print("이메일 형식이 맞습니다.")
