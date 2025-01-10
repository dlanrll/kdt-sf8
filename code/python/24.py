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