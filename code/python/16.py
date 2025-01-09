# 전역변수
quantity = 10

def get_price(price):
    return price * quantity

print(f"{quantity}개의 가격은 {get_price(5000)}입니다.")

# 지역변수
def oneUp():
    x = 0
    x += 1
    return x 

print(oneUp())


# 변수의 유효 범위
amount = 10

def price_sum(price):
    amount = 7
    return price * amount

result = price_sum(2000)
print(result)

# global 키워드
x = 0
def oneUp():
    global x # 함수 내에서 전역변수 "변경"이 이루어질 예정 힌트
    x += 1
    return x

print(oneUp())
print(oneUp())
print(oneUp())
print(x)

