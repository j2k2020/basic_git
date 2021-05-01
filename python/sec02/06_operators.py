# 연산자
# 산술 연산자: + - * / //(나눗셈, 몫) %(나머지) **(지수)
# 관계 연산자: == != > < >= <=
# 논리 연산자: and or not
# 비트 연산자: & (AND) | (OR) ^(XOR)


# print(20 // 7) # 나눗셈(몫)
#  print(20 % 7) # 나눗셈
#  print(2 ** 3) # 지수

# 연습문제
# 현금이 5,000원 있고
# 사탕 가격이 120원
# 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?
cost=5000
candy=120
totalCdy=cost//candy
# chang=cost-totalCdy 틀렸음
chang=cost%candy
print("사탕의 개수:",totalCdy)
print("나머지 돈:",chang)

