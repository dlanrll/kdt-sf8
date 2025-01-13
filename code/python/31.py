# 오버라이딩: 자식 클래스에서 부모클래스의 메서드를 재정의
# i) 부모클래스의 메서드 내용을 자식 클래스에서 완전히 바꿔야할 때
# ii) 부모클래스의 메서드 내용을 그대로 실행하되, 자식클래스의 메서드에서 추가적인 작업이 더 있을 때


class Parent:
    def greet(self):
        print("안녕, 부모 클래스")


class Child(Parent):
    def greet(self):
        # super().greet()
        print("안녕, 자식 클래스")


p = Parent()
c = Child()
p.greet()
# 안녕, 부모 클래스
print()
c.greet()
# 안녕, 부모 클래스
# 안녕, 자식 클래스

