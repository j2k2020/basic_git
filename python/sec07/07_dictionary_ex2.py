# 영어사전

ek_dic = dict()

# 단어 등록
while True:
    eng = input("\n영어 단어 등록 (종료는 quit): ")

    if eng == "quit":
        break
    elif eng not in ek_dic:
        kor = input("%s의 뜻 입력 (종료는 quit): " % eng)
        ek_dic[eng] = kor
    else:
        print("%s는 이미 등록된 단어 입니다." % eng)
print()

# 단어검색
while True:
    eng = input("검색할 단어 입력(종료 quit): ")

    if eng == "quit":
        break
    elif eng in ek_dic:
        print("%s의 뜻은 %s입니다." % (eng, ek_dic[eng]))
    else:
        print("%s는 사전에 없는 단어입니다." % eng )
print("\n종료합니다.")