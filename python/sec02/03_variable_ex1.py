# 변수 선언 후 값 저장하고 출력
name = "홍길동"
stdNo = 2021001
year = 4
socor = "A"
age = 93.5

# print("성명: "+name)
# print("학번: "+str(stdNo))
# print("학년: "+str(year))
# print("학점: "+socor)
# print("평균: "+str(age))

# print("성명: ",name)
# print("학번: ",stdNo)
# print("학년: ",year)
# print("학점: ",socor)
# print("평균: ",age)

# 포맷 코드 사용 출력: print("서식" % 값)
print("성명: %s" % name)
print("학번: %d" % stdNo)
print("학년: %d" % year)
print("학점: %c" % socor)
print("평균: %.2f" % age)

# 퍼센트로 %로 출력
print("10%")
rate = 80
print("출석률: %d%%" % rate)

#2개 이상의 값 출력
total = 250
avg = 83.33
print("총합: %d, 평균: %.2f" % (total, avg)) # 반드시 괄호로 묶는다(괄호()없으면 오류)