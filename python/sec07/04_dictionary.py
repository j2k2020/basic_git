"""
딕셔너리 (Dictionary)
 - 키(key)와 값(value)의 한 쌍을 요소로 갖는 자료형
 - 딕셔너리 = {키1:값1, 키2:값2, ...}
 - d = {1:'a', 2:'b', 3:'c'}

딕셔너리의 특징
-순서가 없다
-인덱스로 접근할 수 없다
-key를 통해서만 접근 가능
-key는 숫자, 문자 다 가능
-key:value 한 쌍을 item이라고 한다
-쉽표(,)로 item 구분
-중과로 {}사용

딕셔너리의 주요 함수
-딕셔너리 변수.key(): key만 추출해서 리스트로 반환: [1,2,3]
-딕셔너리 변수.values(): value만 추출해서 리스트로 반환: ['a','b','c']
-딕셔너리 변수.items(): (key:value)의 튜플을 추출해서 리스트로 반환
    - [(1:'a'), (2:'b'), (3:'c')]

#딕셔너리 만드는 방법
(1) {] 중괄호 안에 키:값 형식으로 저장
(2) 빈 딕셔너리 만들어서 추가: {}만 저장
(3) dict() 함수 사용
"""

# (1) {] 중괄호 안에 키:값 형식으로 저장
scores = {'kor':90, 'eng':88, 'math':95}
print(scores)

# (2) 빈 딕셔너리 만들어서 추가: {}만 저장
students = {} # {}만 생성
students['name'] = '홍길동' # key추가
students['age'] = 27 # value추가
print(students)

# (3) dict() 함수 사용
person = dict()
print(person) # {}만 생성
# key와 value추가
person["이름"] = "홍길동"
person["키"] = 175
person["몸무게"] = 78.2
print(person)

person2 = dict(이름='이몽룡', 키=170, 몸무게=90)
print(person2)

person3 = dict(zip(['이름', '키', '몸무게'], ['성춘향', 160, 50]))  # zip([키],[값])
print(person3)

# 길면 여러 줄로 입력해도 됨
naver = {
    'name': "naver",
    'url': 'www.naver.com',
    'userid': 'nv',
    'password': '1234'
}

google = {
    'name': "google",
    'url': 'www.google.com',
    'userid': 'gg',
    'password': '2233'
}
print(naver)
print(google)











