# 예외처리

try:
    x = int(input("숫자를 입력하세요."))
    result = 10 / x
except ZeroDivisionError as e:
    print("예외메세지 : ", e)
except ValueError as e :
    print("예외메세지 : ", e)
else:
    print(f"result는 {result}")
finally:
    print("프로그램을 종료합니다.")

# raise

def divide (a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

try:
    result = divide(10, 2)
except ZeroDivisionError as e :
    print("예외발생", e)
else:
    print(result)


