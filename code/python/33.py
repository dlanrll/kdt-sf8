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
    convertion_rate = 1.60934

    