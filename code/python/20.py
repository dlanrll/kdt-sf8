"""
# 람다식
def add(x, y):
    return x + y
print(add(3, 4))


add2 = lambda x, y: x + y  #람다식
print(add2(4, 5))

# 매개변수가 1개인 람다식
square = lambda x: x**2
print(square)
print((lambda x: x**2)(5))

# 매개변수가 2개인 람다식
mul = lambda x, y: x * y
print(mul(3, 7))
print((lambda x, y : x * y)(3, 7))

# 람다 함수를 매개 변수로 전달

# call(): 함수를 인수로 받아서 그 함수를 10번 호출하는 함수
def call(func):
    for _ in range(10):
        func()

# hello(): 일반 함수로, "안녕" 문자 입력
def hello():
    print("안녕")

# 람다식으로 정의된 함수 hello2
hello2 = lambda: print("하이")

call(hello)  # call 함수에 hello 함수를 전달해서 10번 실행
call(hello2) # call 함수에 hello2 람다식을 전달해서 10번 실행


# map, filter 와 함께 쓰는 람다식
# 1. 람다식 with map()
def square(x) : # 일반함수
    return x ** 3

numbers = [2, 4, 6, 8, 10] 
print(list(map(square, numbers))) # 일반식
print(list(map(lambda x : x ** 3, numbers))) # 람다식

# 2. 람다식 with filter()
def even_number(x):
    return x % 2 == 0


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(even_number, numbers2)))  # 일반함수
print(list(filter(lambda x: x % 2 == 0, numbers2)))  # 람다식


# 3. map, filter 두 개를 람다식과 함께 사용
# 3-1. 짝수만 남겨서 -> filter
# filter(lambda x: x % 2 == 0, numbers2)
# 3-2. 그 제곱을 계산 -> map

even_squared_nums = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers2)))
print(even_squared_nums)
"""

weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]

# 도시별 평균 기온 계산
def calculate_average_temperature(city):
    temperatures = list(map(lambda x: x[2], filter(lambda x: x[1] == city, weather_data)))
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        print(f"{city}의 평균 기온: {avg_temp:.2f}℃")
    else:
        print(f"{city}의 데이터가 없습니다.")

# 도시별 최고/최저 기온 찾기
def find_max_min_temperature(city):
    temperatures = list(map(lambda x: x[2], filter(lambda x: x[1] == city, weather_data)))
    if temperatures:
        print(f"{city}의 최고 기온: {max(temperatures):.2f}℃, 최저 기온: {min(temperatures):.2f}℃")
    else:
        print(f"{city}의 데이터가 없습니다.")

# 도시별 강수량 분석
def analyze_rainfall(city):
    rainfalls = list(map(lambda x: x[3], filter(lambda x: x[1] == city, weather_data)))
    if rainfalls:
        total_rainfall = sum(rainfalls)
        rainy_days = len(list(filter(lambda x: x > 0, rainfalls)))
        print(f"{city}의 총 강수량: {total_rainfall:.2f}mm, 강수량이 있었던 날: {rainy_days}일")
    else:
        print(f"{city}의 데이터가 없습니다.")

# 데이터 추가
def add_weather_data():
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시를 입력하세요: ")
    temperature = float(input("평균 기온을 입력하세요 (℃): "))
    rainfall = float(input("강수량을 입력하세요 (mm): "))
    weather_data.append([date, city, temperature, rainfall])
    print(f"{city}의 날씨 데이터가 추가되었습니다.")

# 전체 데이터 출력
def print_all_data():
    print("현재 저장된 날씨 데이터:")
    for entry in weather_data:
        print(f"날짜: {entry[0]}, 도시: {entry[1]}, 평균 기온: {entry[2]}℃, 강수량: {entry[3]}mm")

# 메인 프로그램
def main():
    while True:
        print("\n[날씨 데이터 분석 프로그램]")
        print("1. 평균 기온 계산")
        print("2. 최고/최저 기온 찾기")
        print("3. 강수량 분석")
        print("4. 날씨 데이터 추가")
        print("5. 전체 데이터 출력")
        print("6. 종료")

        choice = input("원하는 기능의 번호를 입력하세요: ")

        if choice == "1":
            city = input("도시 이름을 입력하세요: ")
            calculate_average_temperature(city)
        elif choice == "2":
            city = input("도시 이름을 입력하세요: ")
            find_max_min_temperature(city)
        elif choice == "3":
            city = input("도시 이름을 입력하세요: ")
            analyze_rainfall(city)
        elif choice == "4":
            add_weather_data()
        elif choice == "5":
            print_all_data()
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 프로그램 실행
main()

