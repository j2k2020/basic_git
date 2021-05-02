# 1.temp이름의 빈 딕셔너리 생성

# 2.아이스크림의 이름 희망가격을 딕셔너리로 구성: icecream
# 이름   희망가격
# 메로나  1000
# 폴라포  1200
# 빵빠레  1800

icecream = { '메로나':1000, '폴라포':1200, '빵빠레':1800}
print(icecream)


# 3. icecream 딕셔너리에 항목 추가
# 죠스바 1200
# 월드콘 1500
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream)

# 4. icecream 딕셔너리에서 메로나 가격 출력
# 메로나 가격: 1000
print('메로나 가격: ', icecream['메로나'])

# 5. icecream 딕셔너리에서 메로나 가격을 1300으로 수정
icecream['메로나']=1300
print('메로나 가격: ', icecream['메로나'])

# 6. icecream 딕셔너리에서 가격 정보만 추출해서 출력
for value in icecream.values():
    print(value, end=' ') #end=''를 사용해서 한 줄로 출력

print("\n-------------------------------")
print('총 합: ', sum(icecream.values()))