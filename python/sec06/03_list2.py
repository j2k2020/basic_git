# 리스트에서 요소 제거
# remove()
# 리스트에서 값에 해당되는 요소 제거
"""
리스트.remove(값)
동일한 값이 여러개 있는 경우 첫 번째 값만 제거
모든 요소를 제거하려면 for문 사용
모든 요소 제거: clear() (빈 리스트만 남음)

pop():꺼내오다
리스트.pop(): 리스트의 마지막 요소를 반환하고 삭제
리스트.pop(인덱스): 인덱스 위치에 있는 요소 반환하고 삭제
"""

# n = [1,2,3,3,4,5,4,3]
# n.remove(4) #동일한 요소 4가 2개가 존재: remove(4) 첫 번째 4만 제거
# print(n)
import nt

n = [1,2,3,3,4,5,4,3]
count = n.count(3)
for i in range(count):
    n.remove(3)
    print("3을 삭제: ",n) #삭제될 때마다 출력

print(n) #최종  리스트 확인
# 주의
# 리스트의 모든 요소가

# pop(): 리스트의 마지막 요소 반환하고 삭제
x=['a','b','c','d']
y= x.pop()
print(y)
print(x)

x.pop()
x.pop()
x.pop()
print(x)
# 계속 pop()해서 더 이상 요소가 없으면 빈 리스트
# 리스트가 비었는데 pop() 하면 오류 발생
x.pop() #IndexError: pop from empty list