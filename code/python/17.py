# 매개변수
# 기본 매개변수
# 주의, 기본값이 있는 매개변수는 반드시 맨 뒤에 와야함
# + 설명을 덧붙이자면 만약 print(8)만 오면 이게 txt인지 count의 값인지 컴퓨터는 인지하지 못하니까~
def pr_str(txt, count):
    print(txt, count)

pr_str("하이", 3)
pr_str("무기다", 5)


def pr_str(txt = "이무기는 물속에서 100년을 살아", count = 100):
    print(txt, count)

# 반복문에서 "_" : 반복변수를 사용하지 않을 때 사용하는 관례적인 이름

pr_str()
pr_str("하이", 3)
pr_str("무기다")

# 기본 매개변수
# 주의. 기본값이 있는 매개변수는 맨 뒤에 와야 함
def pr_str(txt="안녕하세요", count=1):
    # print(txt, count)
    for _ in range(count):
        print(txt)

    # 반복문에서 "_": 반복변수를 사용하지 않을 때 사용하는 관례적인 이름


pr_str()
pr_str("하이", 3)
pr_str("안녕", 7)
pr_str("빠이")

# 함수 호출 키워드
def intro(name, age, city):
    print(f"이름은 {name}이고, 나이는 {age}이고, 사는 곳은 {city}입니다.")

intro("Allie", 23, "Seoul")
intro(city="Seoul", name="Allie", age = 23)
intro("Allie", )

# 가변 매개 변수
def calc_avg(*acgs):
    print(args)  # tuple

    total = 0
    for i in acgs:
        total += 1
    avg = total / len(acgs)

    return avg

print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8))
print(calc_avg(10, 20, 30))

# 다른예시
def text_def(a, b, *args):
    print(f"a: {b}")
    print(f"b: {a}")
    print(f"args: {args}")

text_def("HI", 100, 9, 7, 5, 3, 1)

# 가변 키워드 매개변수
def print_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}의 값은 {value} 입니다.")

print_info(name="홍길동", city = "서울", gender = "남자")
print_info(name="성추냥", city = "부산", age = 81)
