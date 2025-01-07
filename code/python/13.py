# 리스트 내포
# 파이썬에서 리스트를 간결하게 생성하는 문법
'''
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)

squares2 = [n**2 for n in range(1, 6)]
print(squares2)

#조건문과 함께 사용
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)

#구구단 실습
numbers = [7]
total = 0
for num in numbers :
    total += num
    print("현재 total >> ", total)
print(f"합계는 {total}입니다.")

for i in range(1)

fruits = {"apple": 95, "banana": 105, "cherry":50}
rnrneks = input("몇단을 출력할까요? : ")

for i in range : 
    print(f"{fruit}의 칼로리는 {fruits[fruit]}Kcal 입니다.")
else :
    print("과일이 존재하지 않습니다.")

# 조건문과 함께 사용

#실습. 정수 합 계산
#1부터 사용자가 입력한 수까지 홀수의 합 구하기
while True:
    user_input = input("어디까지 계산할까요?: ")

    number = int(user_input)
    if number == (range(1, 6) if x % 2 =! 0) :
        continue

    total_sum = sum(number)
    print(f"1부터 {number}까지의 합: {total_sum}")'''

#if와 elif의 차이는 if와 elif를 동시에 썼을 때 그 조건이 중첩일 경우 다음 코드로 내려가지 않음
#결론 : 조건들이 겹치지 않는(상호베타적) 상황일 때는 if, elif, else를 작성해도 되지만
# 그렇지 않을 경우에는 if를 작성할 것