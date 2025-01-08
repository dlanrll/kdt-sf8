# 리스트 내포
# 파이썬에서 리스트를 간결하게 생성하는 문법

numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)

squares2 = [n**2 for n in range(1, 6)]
print(squares2)

#조건문과 함께 사용
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)

#구구단 실습
multiple = int(input("몇단을 출력할까요?: "))

for i in range(1, 10):  # 1부터 9까지 반복
    print(f"{multiple} x {i} = {multiple * i}")

# 실습, 정수 합 계산
# 방법1
n = int(input("어디까지 계산할까요? : "))
odd_sum = sum(i for i in range(1, n + 1) if i % 2 != 0)
print(f"1부터 {n}까지의 홀수의 합: {odd_sum}")

# 방법2
n = int(input("어디까지 계산할까요? : "))
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0: 
        odd_sum += i
print(f"1부터 {n}까지의 홀수의 합: {odd_sum}")

# 실습, 평균값 구하기
students = {
    "학생1" :{"국어":83, "영어":92, "수학":88},
    "학생2" :{"국어":90, "영어":79, "수학":86},
    "학생3" :{"국어":88, "영어":86, "수학":94}
}

subjects = ["국어", "영어", "수학"]
averages = {}

for subject in subjects:
    total = sum(student[subject] for student in students.values())
    averages[subject] = total / len(students)


print("과목별 평균 점수:")
for subject, avg in averages.items():
    print(f"{subject}: {avg:.2f}점")

    total_sum = sum(averages)
    print(f"1부터 {averages}까지의 합: {total_sum}")


'''if와 elif의 차이는 if와 elif를 동시에 썼을 때 그 조건이 중첩일 경우 다음 코드로 내려가지 않음
결론 : 조건들이 겹치지 않는(상호베타적) 상황일 때는 if, elif, else를 작성해도 되지만
그렇지 않을 경우에는 if를 작성할 것'''

# 학점 평균내기 아이고 강사님 코드

