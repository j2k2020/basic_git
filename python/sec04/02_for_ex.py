# 다음과 같은 명단에서 이름이 명단에 있는지 검색
# ["홍길동","이몽룡","성춘향","변학도"]

# 이름 입력: 홍길동 입력한 경우
# 명단에 있습니다.
#
# 이름 입력: 박지성 입력한 경우
# 명단에 없습니다.

name = input("이름을 입력하세요:")
for Name in ["홍길동","이몽룡","성춘향","변학도"]:
    if name == Name:
        find = True
        break
    else:
        find = False

if find:
    print("명단에 있습니다.")
else:
    print("명단에 없습니다.")
