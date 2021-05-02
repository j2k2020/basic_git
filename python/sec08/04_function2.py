# 키워드 인수 예제
def student_info(name, age, gender):
    student = {
        'name': name,
        'age': age,
        'gender': gender
    }
    return student

# 출력 함수에 기입하는 순서는 실제 출력 순서와 상관 없다
print(student_info(age=23, gender='F', name='kim'))
print(student_info('lee', gender='M', age=33))

# 위치 인수가 매개 변수 뒤에 나오며 안된다?!
# print(student_info(gender='M', age=33, 'lee'))