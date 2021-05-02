# 가위바위보 게임
# 홍길동 입력: 바위 입력한 경우
# 이몽룡 입력: 가위
# 홍길동이 이겼습니다.

# choice=input("1:가위, 2:바위, 3:보 입력하세요: ")
print("1:가위, 2:바위, 3:보 숫자로 입력한 가위바위보 게임\n")

hong: int = int(input("홍길동 입력: "))
mong: int = int(input("이멍령 입력: "))

if hong > mong:
 print("홍길동이 이겼습니다.")
elif hong < mong:
 print("이멍령이 이겼습니다.")
else:
  print("비겼습니다.")