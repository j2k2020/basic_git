"""
지역변수: 함수 내부에서 정의된 변수
 - 함수 내에서만 사용 가능
 - 함수 호출 시 생성되고 함수가 종료되면 소멸(더 이상 사용 불가능)
 - 함수의 매개변수도 함수 내에서만 사용할 수 있는 지역변수
"""
def show():
    a = 1 #show() 함수 내에서 정의된 지역변수: 함수 내에서만 사용 가능
    print(a)

show()
# print (a) #함수 외부에서 사용 불가

def show2(b): #매개변수 b도 함수 내에서만 사용가능한 지역변수
    b = b +1
    print(b)

show2(10)
# print(b)  #함수 외부에서 사용 불가



"""
전역변수
 - 함수 외부에서 정의된 변수
 - 프로그램 내의 모든 곳에서 사용 가능
 - 함수 내에서 전역 변수의 값을 변경하려면 global 키워드 사용
"""

x = 1 # 함수 밖에서 정의된 전역 변수 (모든 곳에서 사용 가능)
print(x)

def show3():
    print(x) # x는 전역변수라 함수 내에서도 사용 가능

def add():
    print(y) # y는 전역변수라 함수 내에서 사용 가능
             # 전역 변수가 정의된 위치보다 앞에서도 사용 가능(앞/뒤 상관 없음)

y = 2  # 함수 밖에서 정의된 전역 변수

show3()
add()

def show4():
    global  x
    x = x + 100 #전역변수 값을 변경하려면 global 키워드를 사용해야 됨
    print(x) #전역변수이므로 함수 내에서도 사용 가능