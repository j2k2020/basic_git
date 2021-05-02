# 파일 입출력
"""
파일 입출력하기 위해서 open() 함수 사용
파일 객체 = open(파일명, 파일 열기 모드)
 - 파일이 저장된 곳 참조(포인터 역할)
파일 열기 모드에 따라 파일 생성/읽기/쓰기 추가 기능 수행
  r : read (읽기만 가능)
  w : write (쓰기만 가능)
  a : append (파일 끝에 내용 추가)

파일 닫기
 파일 작업이 끝나면 close() 함수로 열려 있는 파일 객체 닫음

파일 생성
 파일을 쓰기 모드(w)로 연다
 해당 파일이 존재하지 않으면 새로 생성하고
 존재하면 덮어 쓴다(기존 내용 없어짐)
"""

# 파일 생성: 파일명만 적으면 현재 디렉터리에 생성
f = open("file1.txt", 'w')
f.close()

# 파일은 실행 시 ctrl+Enter 사용하지 않고
# 파일 단위로 실행: Run

# file1.txt가 존재하는데
# 동일한 이름으로 다시 생성하면
# 기존 파일 덮어쓰게 되어서 내용이 삭제됨

# 존재하지 않는 디렉터리에 생성하면 오류 발생
f = open("C:/python/file2.txt", 'w')
f.close()

# 주의!
# 경로명에 역슬래시(\) 사용하면 오류
# f = open("C:\python\file2.txt", 'w')
# f.close()

# 경로명에 역슬래시(\) 사용하고 싶으면, 2번(\\) 사용하면 오류 없음
f = open("C:\\python\\file3.txt", 'w')
f.close()

# 파일에 데이터 쓰기: 쓰기 모드(w)로 열고
# 파일 객체의 write() 메소드로 출력값을 파일에 기록
data = 'hi'
f = open("file2.txt", 'w')
f.write(data)
f.close()


# 한글 사용 시
# PCham에서 열려면 워크스페이스 경로에서 txt인코딩 타입을 utf=8로 변경해주기
data2 = '안녕하세요'
f = open("file2.txt", 'w')
f.write(data2)
f.close()

# 한글 데이터가 포함된 파일을 생성하며 인코딩이 ANSI로 저정
# 파이참에서 열면 한글 깨짐 현상 발생
# 메모장에서는 문제 없이 한글 출력
# 다른 이름 저장: 인코딩 UTF-U로 저장하면 됨

# 파일 생성 시 인코딩을 UTF-8 설정
data = '안녕하세요'
f = open("file3.txt", 'w', encoding='utf-8')
f.write(data)
f.close()

# 파일에 쓰기
f = open("file4.txt", 'w', encoding='utf-8')

for i in range(1,11):
    data = str(i) + "행\n"
    f.write(data)


