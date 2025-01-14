# calculator.py


# 함수
def add(x, y):
    return x + y


def sub(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        print("나눌 수 없음")
    else:
        return x / y

# 변수
PI = 3.141592
e = 2.718

# 클래스
class Calculator:
    def multiply(self, a, b):
        return a * b
    
    def square(self, x):
        return x ** 2