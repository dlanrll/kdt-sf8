# 다중 상속
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count


class Car(Engine, Wheels):  # 다중상속
    def __init__(self, horsepower, wheel_count):
        # 부모클래스의 생성자를 호출해서 horsepower, wheel_count 를 초기화
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, wheel_count)

    def info(self):
        print(
            f"이 자동차는 {self.horsepower} 마력과 {self.wheel_count} 개의 바퀴를 가짐"
        )


car = Car(100, 4)
car.info()
print(Car.mro())  # mro() : 클래스 계층구조를 나타냄
# 

# MRO (메서드 해석 순서, Metgod REsolution Order)
# : "다중상속"에서 메서드 호출 순서를 결정하는 규칙
# ex. Car 클래스에서 메서드를 찾을 때 어떤 순서로 부모 클래스들을 탐색할지 결정

# 참고, <class 'object'>
# : 모든 클래스는 object 클래스를 상속하므로 object 클래스를 맨 마지막으로 생성


