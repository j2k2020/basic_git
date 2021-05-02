# readline(): 1개 행씩 읽어 오기( 1행 끝에 '\n')

print("파일 전체 읽기")
f = open("file4.txt", 'r')
lines = f.readlines()  # 리스트로 생성

for line in lines:
    print(line, end=' ')
f.close()

# append(): 파일 끝에 추가
# 파일 열기 모드: a
f = open("file2.txt", 'a')

data = '\nPython Programming'
f.write(data)

# 읽기 모드로 바꾸어서 파일 다시 읽고
# 내용 읽어 오기
f = open("file2.txt",'r',encoding='utf=8')
print(f.read())
f.close()