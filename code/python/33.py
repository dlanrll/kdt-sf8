# 클래스 매서드

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)
    
p1 = Person("김철수", 20)  # 기본 생성자로 객체 생성
p2 = Person.from_birth_year(
    "홍길동", 1990
)

print(f"{p1.name}: {p1.age}")
print(f"{p2.name}: {p2.age}")


# ii) 유틸리티 함수 구현
# ex. 마일 단위를 킬로미터 단위로 변환하는 예시
class Converter:
    conversion_rate = 1.60934   # 클래스 변수

    @classmethod
    def miles_to_km(cls, mile):
        return mile * cls.conversion_rate
    
my_mile = 7
print(Converter.miles_to_km(my_mile))
# 객체 생성없이 바로 클래스. 메서드

# 인스턴스(객체)마다 수행해야하는 작업이 동일한 경우
# 단위변환, 문자열 대소문자 반환, 리스트에서 중복 값 제거 등...


# iii) 클래스 변수 수정
# ex. 모든 인스턴스가 공유하는 값을 관리해야 할 때
class Counter:
    count = 0  # 클래스 변수

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


print(Counter.get_count())
Counter.increment()
print(Counter.get_count())
Counter.increment()
print(Counter.get_count())

# iv) 자식 클래스의 정보 유지
class Animal:
    species = "동물"

    @classmethod
    def get_species(cls):
        # cls: 메서드를 호출한 실제 클래스
        # -> 상속 관계에서 자식 클래스의 값을 올바르게 찾아서 보여줌
        return cls.species


class Dog(Animal):
    species = "진돗개"


print(Animal.get_species())  # 동물
print(Dog.get_species())  # 진돗개

# Class Method 정리
# - @classmethod 데코레이터 사용
# - 첫번째 매개변수 cls(클래스) 받음
# - (인스턴스를 생성하지 않고) 클래스 자체를 통해 호출 가능
# - 클래스 속성에 접근하거나 수정할 때 사용 가능 (iii 예시)
# - 상속시 cls 는 하위 클래스 참조(가르킴, 바라봄) (iv 예시)

# vs. Insatnce Method 정리
"""
class ExClass:
    def instance_method(self):
        return "인스턴스 메서드임"
"""
# - 일반적인 메서드로, 첫번째 매개변수로 self(자기자신, 호출된 인스턴스(객체))
# - 인스턴스를 생성한 후에, 인스턴스를 통해 호출하고 인스턴스 속성에 접근 가능
# - 객체의 속성(상태)을 변경하거나 접근할 때 사용


