# MRO

class A :
    def speak(slef):
        print("A 클래스")

class B(A) :
    def speak(slef):
        print("B 클래스")

class C(A) :
    def speak(slef):
        print("C 클래스")

class D(B, C):
    pass # 아무것도 안 하는 키워드

d = D()
# A, B, C 클래스 모두 speak() 메서드를 가지고 있는데, 과연 여기서 어떤 클래스의 speak()가 호출?
# mro 원칙에 따른 클래스의 메서드가 호출이 됨

d.speak() # B 클래스
print(D.mro()) # D > B > C > A > object

# 다중상속의 유의점 : 이름이 충돌 문제가 있다

