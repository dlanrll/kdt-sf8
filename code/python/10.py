# 조건문
age = 17

if age < 20:
    print("나는 미성년자입니다")

if age >= 20:
    print("성인 입니다")

print(f"나이는 {age}(세)입니다.")


# else문
if age < 20:
    print("미성년자입니다")
else :
    print("성인입니다")

# elif 문
age = int(input("나이를 입력하세요"))

if age < 20 :
    print("10대입니다")
elif age < 30 :
    print("20대입니다.")
elif age < 40 :
    print("30대입니다.")
elif age < 50 :
    print("54대 이상입니다.")
else :
    print("50대 이상입니다.")

# if문 실습
# 비밀번호 abc123을 입력했을 때 "비밀번호가 맞습니다" 출력시켜주기
password = input("비밀번호를 입력하세요.")

if password == "abc123":
    print("비밀번호가 맞습니다.")  

# 짝수 숫자를 입력했을 때 "짝수입니다." 출력시켜주기
number = int(input("숫자를 입력하세요."))
if number % 2 == 0 :
    print("짝수입니다.")


# if문 실습
# 비밀번호 abc123을 입력했을 때 "비밀번호가 맞습니다" 출력시켜주기
password = input("비밀번호를 입력하세요.")

if password == "abc123":
    print("비밀번호가 맞습니다.")
else :
    print("비밀번호가 틀렸습니다.")    

# 짝수 숫자를 입력했을 때 "짝수입니다." 출력시켜주기
number = int(input("숫자를 입력하세요."))
if number % 2 == 0 :
    print("짝수입니다.")
else:
    print("홀수입니다.")

# elif 실습
# 점수를 입력 받아 점수에 다라 A~F 학점으로 나누기
score = int(input("점수를 입력하세요 :"))

if score < 60 :
    print("학점 : F")
elif score < 70 :
    print("학점 : D")
elif score < 80 :
    print("학점 : C")
elif score < 90 :
    print("학점 : B")
else :
    print("학점 : A")

'''
얕은 복사 vs. 깊은 복사

얕은 복사 (Shallow Copy) 
- 객체의 참조만 복사 → 원본과 복사본이 같은 데이터를 공유  
- 내부 중첩 객체는 공유됨 → 한쪽 수정 시 다른 쪽도 영향 받음

깊은 복사 (Deep Copy)
- 객체의 모든 계층을 새로 복사 → 원본과 복사본이 독립적 
- 내부 중첩 객체도 별도로 복사 → 서로 영향 없음

Python에서 사용하는 메서드

1. 얕은 복사
   - `copy.copy()`  
   - 슬라이싱 (`list_a[:]`)  
   - `list()` / `dict()` 생성자  

2. 깊은 복사
   - `copy.deepcopy()`  
'''

# 중첩 조건문
# 불리언(Boolean) : 참과 거짓을 나타내는 데이터 타입 (자료형, 값이 두 개 뿐이다)
# 참 : True, 거짓 : False

is_login = True
role = "admin"

if is_login :                            # if is_login == True와 같음, 불필요한 연산은 줄일것
    print("로그인 상태입니다")
    if role == "admin" :
        print("관리자 권한을 갖습니다.")
    elif role == "editor" :
        print("편집자 권한을 갖습니다.")
    else :
        print("일반 사용자입니다.")
else : 
    print("로그인이 필요합니다.")

# 삼항 연산자
age = 18
status = "성인" if age >= 20 else "미성년자"
print(status)

number = 7
result = "짝수" if number % 2 == 0 else "홀수"
print(result)

a, b = 5, 8
max_value = a if a > b else b
print(max_value)

# 중첩 삼항 연산자
score = 81
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")

# 조건문에서 in 연산자 활용

user = ["sean", "Linda", "Allie", "dlanrl"]
username = input("Name >> ")

if username in user : 
    print(f"환영합니다, {username}님!")
else :
    print("등록되지 않은 사용자입니다. 회원가입을 진행해주세요.")


# 중첩 조건문 실습
age = int(input("나이를 숫자로 입력해주세요: "))
pay = input("결제 방법을 입력해주세요 (현금 또는 카드): ")
if pay == '카드':
    if age < 8:
        fare = 0
    elif age < 14:
        fare = 720
    elif age < 20:
        fare = 720
    elif age < 75:
        fare = 1200
    else:
        fare = 0     
elif pay == '현금' :
    
    if age < 8:
         fare = '무료'
    elif age < 14:
        fare = 450
    elif age < 20:
        fare = 1000
    elif age < 75:
        fare = 1300
    else:
        fare = '무료'
print(f"{age}세의 {pay}요금은 {fare}원입니다.")


''' 아이고 리더님이 작성하신 코드, 공부해보기
pay_list = [[0, 450, 720, 1200, 0],
            [0, 450, 1000, 1300, 0]]

years = input("나이를 숫자로 입력해 주세여: ")
years = int(years)

how = input("결재방법을 입력해 주세여 (카드 또는 현금): ")

code = -1 
result = 0

code = 0 if how == "카드" else 1\
         if how == "현금" else -1
        
result = pay_list[code][0] if years < 8 else pay_list[code][1]\     #역슬래시는 한 문장으로 쭉 가고 싶다는... 코드를 가독성 있게 이쁘게 쓰고 싶을 때 씀
                           if years < 14 else pay_list[code][2]\    #다음 줄에 있는 내용이 한 문장으로 쭉 이어진다
                           if years < 20 else pay_list[code][3]\
                           if years < 75 else pay_list[code][4]

if code == 0:
    print(f"{years}세의 카드요금은 {result}입니다")
else:
    if code == 1:
        print(f"{years}세의 현금은 {result}입니다")
    else:
        print("결제방법을 잘못 입력하셨습니다")
'''


# 과일의 칼로리를 담는 딕셔너리 생성
fruits = {"apple": 95, "banana": 105, "cherry":50}
fruit = input("과일을 영문으로 입력하세요. : ")

if fruit in fruits : 
    print(f"{fruit}의 칼로리는 {fruits[fruit]}Kcal 입니다.")
else :
    print("과일이 존재하지 않습니다.")