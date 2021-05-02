# 문자열 인덱싱(indexing)
# 인덱스로 문자의 위치를 나타내는 것
# 인덱스(첨자): 문자의 위치, 0부터 시작
# string[a]: 인덱스 0번째 문자(첫 번째 문자)
# string[-1]: 마지막 문자

# 슬라이싱(slicing)
# 문자열 중에서 일부분을 추출하는 것 (잘라내는 것)
# 인덱스 사용
# string[0:n] : 0부터 n-1번째 까지의 문자열 출력
# string[n:] : 01부터 끝까지
# string[-1:] :마지막 문자(마지막에서 끝까지)
# string[:-1] : 처음부터 마지막 -1
# string[:] : 전체 문자열 반환

python = "python programming is fun"
java = "java is also funny"

print(python[5:15])
print(python[:])
print(python[5:])
print(python[:15])
print(python[:-1])
