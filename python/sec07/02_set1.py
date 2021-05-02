#집합(set)
"""
수학의 집합
중복되지 않은 항목들이 모인 것
집합 ={ 항목1, 항목2, .., 항목n}

집합의 특징
순서가 없다: 입력되는 출력되는 순서가 다를 수 있음
동일한 요소(값)이 중복될 수 없다
인덱스 사용 불가
요소 추가/삭제는 가능하지만
집합 안에 변경 가능한 항목을 포함 할 수 없음
 - 리스트는 포함 할 수 없음
 - 튜플은 포함 가능
"""

#집합 만들기
s1 = { 1, 2, 3, 4, 5}
print(s1)
print(type(s1)) #<class 'set'>

#set() 함수 사용해서 집합 만들기
#리스트로 집합 생성
s2 = set([10, 20, 30])
print(s2)

s3 = set((100, 200, 300))
print(s3)

#동일한 요소(값)이 중복될 수 없다
s4 = { 1, 2, 3, 4, 5}
print(s4)
