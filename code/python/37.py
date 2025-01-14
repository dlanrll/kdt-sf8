# 모듈 불러오기: 확장자를 생략하여 파일명으로 불러옴
import calculator

# 모듈의 함수 사용
print(calculator.add(5, 7))  # 12
print(calculator.sub(5, 9))  # -4

# 모듈의 변수 사용
print(calculator.PI)  # 3.141592

# 모듈의 클래스 사용
calc1 = calculator.Calculator()
print(calc1.multiply(4, 3))  # 12
print(calc1.square(4))