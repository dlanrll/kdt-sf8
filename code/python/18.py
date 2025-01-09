# 내장 함수

# abs(정수): 절댓값 구하는 내장함수
print(abs(-77))
print(abs(0))
print(abs(10))


# 만약에, abs() 내장함수가 없었다면?
def my_abs(n):
    if n < 0:  # 음수라면, 양수로 변환하여 반환
        return -n
    else:  # 0 혹은 양수이니 그대로 반환
        return n


print(my_abs(-77))
print(my_abs(0))
print(my_abs(10))

# pow(x, y): x^y 구하는 내장함수
print(pow(10, 2))
print(pow(2, 10))
print(pow(3, 4))

# 만약에, pow() 내장함수가 없었다ㅁㄴ?

city = "서울"
x = [["서울", 10], ["서울", 20], ["부산", 30]]
a = filter(lambda x : x[0] == city, x)
print(list(map(lambda x: x[1], a)))

i = 3.333333333
print(f"{i:.2f}")
# 실습

multiples = [] 
for i in range(1, 31):  
    if i % 3 == 0:  
        multiples.append(i) 

for multiple in multiples:
    print(multiple, end=" ")  
print() 

print("3의 배수의 개수:", len(multiples)) 

# 목록이랑 갯수를 같이 구하는 문제는 list를 쓰는게 유리해요

# 실습 풀이1 sean 리더님 거
def count(num):
    lists = [i for i in range(1, 31) if i % num == 0]
    counts = len(lists)

    return (lists, counts)


n = int(input("1~30 중 몇의 배수가 궁금하신가요? > "))  # 배수
my_lists, my_counts = count(n)  # (리스트, 개수)
print(f"{n}의 배수 목록: {my_lists}")
print(f"{n}의 개수: {my_counts}")

# print(count(n))
# ([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], 10)
# ([4, 8, 12, 16, 20, 24, 28], 7)

# 실습 풀이2


def count(num):
    # 중첩함수 - 해당 함수 안에서만 호출 가능
    def check(x):  # num의 배수인지를 검사하는 함수
        return x % num == 0

    lists = list(filter(check, range(1, 31)))

    return (lists, len(lists))


n = 6
my_lists, my_counts = count(n)  # (리스트, 개수)
print(f"{n}의 배수 목록: {my_lists}")
print(f"{n}의 개수: {my_counts}")

