# 매개변수
# 기본 매개변수
# 주의, 기본값이 있는 매개변수는 반드시 맨 뒤에 와야함
# + 설명을 덧붙이자면 만약 print(8)만 오면 이게 txt인지 count의 값인지 컴퓨터는 인지하지 못하니까~
"""
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


# 과제...
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

def display_vending_machine():
    print("남은 음료수:", vending_machine)

def consumer_action():
    drink = input("마시고 싶은 음료를 입력하세요: ")
    if drink in vending_machine:
        vending_machine.remove(drink)
        print(f"{drink}를 드립니다.")
    else:
        print("해당 음료는 없습니다.")

def owner_action():
    action = input("1. 추가, 2. 삭제 (번호 입력): ")
    if action == "1":
        new_drink = input("추가할 음료 이름: ")
        vending_machine.append(new_drink)
        print(f"{new_drink}가 추가되었습니다.")
    elif action == "2":
        remove_drink = input("삭제할 음료 이름: ")
        if remove_drink in vending_machine:
            vending_machine.remove(remove_drink)
            print(f"{remove_drink}가 삭제되었습니다.")
        else:
            print(f"{remove_drink}는 자판기에 없습니다.")
    else:
        print("잘못된 입력입니다.")

while True:
    display_vending_machine()
    user_type = input("1. 소비자, 2. 주인 (번호 입력): ")
    if user_type == "1":
        consumer_action()
    elif user_type == "2":
        owner_action()
    else:
        print("잘못된 입력입니다.")
    
    if input("계속하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break


"""

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

def display_vending_machine():
    print(f"남은 음료수: {vending_machine}")

def consumer_action():
    drink = input("마시고 싶은 음료를 입력하세요: ")
    if drink in vending_machine:
        vending_machine.remove(drink)
        print(f"{drink}를 드릴게요.")
    else:
        print("해당 음료는 없습니다.")
    display_vending_machine()

def owner_action():
    print("할 일을 선택하세요:")
    print("1. 추가")
    print("2. 삭제")
    action = input("선택: ")

    if action == "1": 
        new_drink = input("추가할 음료 이름을 입력하세요: ")
        vending_machine.append(new_drink)
        print(f"{new_drink}가 추가되었습니다.")
    elif action == "2": 
        remove_drink = input("삭제할 음료 이름을 입력하세요: ")
        if remove_drink in vending_machine:
            vending_machine.remove(remove_drink)
            print(f"{remove_drink}가 삭제되었습니다.")
        else:
            print(f"{remove_drink}는 자판기에 없습니다.")
    else:
        print("잘못된 입력입니다.")
    display_vending_machine()

def main():
    while True:
        display_vending_machine()
        print("사용자 종류를 입력하세요:")
        print("1. 소비자")
        print("2. 주인")
        user_type = input("선택: ")

        if user_type == "1":
            consumer_action()
        elif user_type == "2":
            owner_action()
        else:
            print("잘못된 입력입니다. 1 또는 2를 입력해주세요.")

        continue_program = input("계속하시겠습니까? (y/n): ")
        if continue_program.lower() != 'y':
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()


