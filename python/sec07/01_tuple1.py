# 튜플 (tuple)
"""
리스트와 유사한 집합적 자료형
리스트와 달리 요소 변경 불가: 추가/ 수정/ 삭제 안 됨
소괄호 사용: 튜플 = (1, 3, 5)
colors = ("red","green","blue")
각 요소
내용을 변경할 수 없게 하기 위해서 사용
값이 변하지 않는 데이터에 사용

#튜플 만들기
t1 = (1,2,3) #소괄호 사용
t2 = 4,5,6 #괄호 없이 튜플 생성
t3 = [1,2],[3,4] #리스트로 튜플 생성
t4 = tuple([5,6,7,8]) #tuple() 함수 사용
t5 = t1, (7,8,9) #튜플 내에 다른 튜플 포함 가능
"""

t1 = (1, 2, 3) #소괄호 사용
print(t1)

t2 = 4, 5, 6 #괄호 없이 튜플 생성
print(t2)

t3 = [1, 2],[3, 4] #리스트로 튜플 생성
print(t3)

t4 = tuple([5, 6, 7, 8]) #tuple() 함수 사용
print(t4)

t5 = t1, (7, 8, 9) #튜플 내에 다른 튜플 포함 가능
print(t5)

print(type(t5)) #t5의 타입 보기

#튜플을 리스트로 변환
to_ist1 = list(t1)
print(to_ist1)

t = (1, 2, 3)
print(t[1]) #인덱스 사용 가능
t[0] = 5 #오류 발생
# TypeError: 'tuple' object does not support item assignment

