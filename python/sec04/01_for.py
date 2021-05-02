# for문: 정해진 횟수만큼 반복
"""
for문 형식
for 변수 in 범위 또는 리스트:
    반복 수행되는 문장
"""
for name in ["홍길동","이몽룡","성춘향","변학도"]:
    print(name)



# 1~10 숫자 중에서 홀수만 출력
for i in range(1, 10, 2):
    print(i, end=" ")



# 1~100까지의 합 구하기
# 누적 변수 sumX: 반드시 초기화하고 사용해야 함
sumX = 0
for x in range(1, 101):
    sumX += x
print("1~100합: ", sumX)



# 카운트 다운 프로그램 작성
# 시작 숫자를 입력하시오: 5
# 5 4 3 2 1 발사
#
# 시작 숫자를 입력하시오: 10
# 10 9 8 7 6 5 4 3 2 1 발사
count = int (input("시작 숫자를 입력하세요:"))
for x in range(count, 0, -1):
    print(x, end=" ")
print("발사~")

# 파이썬은 들여쓰기를 잘 지켜야만 한다. 잘 못 하면 출력물이 달라짐