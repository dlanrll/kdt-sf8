# 정보 은닉
class Person:
    def __init__(self):
        # 멤버변수 (_name, _age) 언더스코어?
        # -> protected 접근제어로 간주
        # -> 외부에서 직접 접근하지 않고, 해당/서브 클래스에서 사용
        # "직접 접근" 대신 -> getter/setter 를 이용해서 값을 읽거나/수정하도록 함 -> 데이터 보호
        self._name = ""
        self._age = 0

    def setname(self, name):
        self._name = name

    def getname(self):
        return self._name

    def setage(self, age):
        self._age = age

    def getage(self):
        return self._age


p1 = Person()
p1.setname("흥부")
p1.setage(35)
print("이름: ", p1.getname())
print("나이: ", p1.getage())

p2 = Person()
p2.setname("놀부")
p2.setage(38)
print("이름: ", p2.getname())
print("나이: ", p2.getage())



class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location  # 위치
        self.name = name          # 가게 이름
        self.product = product    # 파는 물건
        self.customer = customer  # 고객의 수

    def print_location(self):
        print(f"위치: {self.location}")

    def change_category(self, new_product):
        self.product = new_product
        print(f"상품이 '{new_product}'(으)로 변경되었습니다.")

    def show_list(self):
        print(f"상품: {self.product}")

    def enter_customer(self):
        self.customer += 1
        print(f"손님 수가 증가했습니다. 현재 손님 수: {self.customer}")

    def show_info(self):
        print(f"위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}")

# Supermarket 클래스 사용 예제
market = Supermarket("마포구 염리동", "마켓원", "음료", 12)

market.print_location()  # 위치: 마포구 염리동
market.show_list()       # 상품: 음료
market.enter_customer()  # 손님 수가 증가했습니다. 현재 손님 수: 13
market.change_category("과자")  # 상품이 '과자'(으)로 변경되었습니다.
market.show_info()       # 위치: 마포구 염리동, 이름: 마켓원, 상품: 과자, 고객수: 13




class HealthStatus:
    def __init__(self, name, hp=100):
        self.name = name    # 이름
        self.hp = hp        # 초기 체력 (기본값: 100)

    def exercise(self, hours):
        self.hp += hours    # 운동 시간만큼 체력 증가
        if self.hp > 100:   # 체력 최대치 제한
            self.hp = 100
        print(f"{hours}시간 운동하다")

    def drink_alcohol(self, glasses):
        self.hp -= glasses  # 술잔 수만큼 체력 감소
        if self.hp < 0:     # 체력 최저치 제한
            self.hp = 0
        print(f"술을 {glasses}잔 마시다")

    def show_status(self):
        status = "나몸짱" if self.hp > 50 else "나약해"
        print(f"{self.name} - hp: {self.hp}")
        print(f"=========================")
        print(f"{status} - hp: {self.hp}")

# 클래스 사용 예제
person = HealthStatus("홍길동")

# 첫 번째 상황
person.exercise(5)  # 5시간 운동
person.drink_alcohol(2)  # 술 2잔 마심
person.show_status()

# 두 번째 상황
person.exercise(1)  # 1시간 운동
person.drink_alcohol(12)  # 술 12잔 마심
person.show_status()
