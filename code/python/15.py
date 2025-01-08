# 함수

# 1. 매개변수 X, 리턴값 X
# 함수정의
def say_hello():
    print("안녕, 세상아")

# 함수 호출
say_hello()

# 2. 매개변수 O, 리턴값 X
# 2-1. 매개변수 하나
def print_getting(name) :  # 함수 정의
    print(f"Hello, {name}")

print_getting("Allie")  # 함수 호출

# 2-2. 매개변수 두개
def gugudan(dan, end):  # 함수 정의
    print(f"{dan}단")

    for i in range(1, end):    # 1~end-1
        print(f"{dan} x {i} ={dan * i}")
gugudan(7, 15) # 함수 호출

# 3. 매개변수 X, 리턴값 O
def mul_numbers(): # 함수 정의
    print("곱셈을 시작합니다")
    return 10*5

result = mul_numbers() # 함수 호출
print(result)

# 3. 매개변수 O, 리턴값 O
def add_numbers(x, y): # 함수 정의
    print("덧셈을 시작합니다")
    return x + y

result2 = add_numbers(40, 50)
print(result2)

# 다양한 타입을 return 하는 함수
# 1. list 타입을 반환하는 함수
# ex. 0부터 제한값(limit) 까지의 짝수를 출력하는 함수

def print_even_numbers(limit):
    return [i for i in range(0, limit) if i % 2 == 0]

print(print_even_numbers(10))

# Dictionary 타입을 반환하는 함수
def print_user_info(name, grade):
    return{"user_name" : name, "user_grade" : grade}

print(print_user_info("Allie", 2))
print(print_user_info("dlanrl",4))

print(set("Hello")) #문자열을 set 타입으로 반환 > 고유한 문자들만 남긴다


def print_unique_char(word):
    return set(word)

print(print_unique_char("Hi, My name is dlanrl"))

# 4. Tuple 타입을 반환하는 함수
# ex. 두 숫자의 합과 곱을 동시에 반환 > (합, 곱)
def culcurate_sum_and_product(a, b):
    return(a + b, a * b)

print(culcurate_sum_and_product(3, 5))
print(culcurate_sum_and_product(5, 6))


#매개변수로 리스트를 받는 함수
def double(nums):
    return[i * 2 for i in nums]

print(double([1, 2, 3, 4]))


# ex. 각 요소를 문자열로 변환하는 함수
def to_string(nums):
    return[str(i) for i in nums]

print(to_string([8, ]))

# Collection (컬렉션)
# 혼합 컬렉션
# ex. 딕셔너리 안에 리스트가 있는 예시
# def split_numbers

# 실습1.
# ex. 두 숫자의 합과 곱을 동시에 반환 > (합, 곱)
def result(x, y):
    if x == y:
        return f"결과(곱): {x * y}"
    else:
        return f"결과(합): {x + y}"
# 사용자 입력 받기
x = int(input("첫 번째 숫자를 입력하세요. : "))
y = int(input("두 번째 숫자를 입력하세요. : "))
# 함수 호출 및 결과 출력
print(result(x, y))

#실습2
def total_price(product, price):
    if price < 20000 :
        return f"{product} 가격 : {price + 2500}원"
    else: return f"{product}가격 : {price}원"

print(total_price("상품1", 30000))
print(total_price("상품2", 15000))

#별찍기 실습
# 별찍기 4번
n = 4  # 줄 개수
for i in range(1, n + 1):  # 1~n까지 반복
    # i번째 줄에 대한 내용

    # 공백 출력
    for j in range(n - i):  # n-i개의 공백이 출력
        print(" ", end="")
        # ex. 1번째 줄: N-1 / 2번째 줄: n-2 / .. / 4번째 줄: N-4

    # 별 출력
    for k in range(2 * i - 1):  # 2*i-1개의 별 출력
        print("*", end="")

    # 내부포문이 종료되는 시점
    print()


# 별찍기 5번
# n = 5  # 줄 개수
n = int(input("줄 개수 입력(홀수만 입력 가능): "))

# 윗 삼각형 (3줄) -> 2+1 -> 5//2 + 1
for i in range(1, (n // 2) + 2):  # 1 부터 N//2+1 까지 반복
    # 공백 출력
    for j in range(0, (n // 2) + 1 - i):  # N//2 + 1 - 줄번호
        print(" ", end="")

    # 별 출력
    for k in range(0, 2 * i - 1):
        print("*", end="")

    print()


# 아래 삼각형 (2줄) -> 2 -> 5//2
for i in range(n // 2, 0, -1):  # N//2부터 1까지 반복
    # 공백 출력
    for j in range(0, (n // 2) + 1 - i):  # N//2 + 1 - 줄번호
        print(" ", end="")

    # 별 출력
    for k in range(0, 2 * i - 1):
        print("*", end="")

    print()


