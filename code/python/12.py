# for 문

# range 함수
for i in range(5) : # range(0,5) : 와 같다
    print(i, end = " ")
print()

for i in range(2, 7) :
    print(i, end = " ")
print()

for i in range(11, 20, 2) :
    print(i, end = " ")
print()

for i in range(10, 0, -3) :
    print(i, end = " ")
print()

# 리스트와 for 문
# 뭔가 관례같은 건데 보통 리스트나 튜플 등은 복수니까 변수 이름을 단수와 복수로 나누어서 함
fruits = ["사과", "바나나", "포도", "체리"]
for fruit in fruits :
    print(fruit, end = "-") # 리스트는 순서가 있는 자료형이다
    # 출력결과 : 사과-바나나-포도-체리- 이렇게 끝까지 '-'가 출력되어 나옵니다
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers :
    total += num
    print("현재 total >> ", total)
print(f"합계는 {total}입니다.")

# 조건문과 함께 사용
for num in numbers :
    if num % 2 == 0:
        print(num, end = " ")
print()

# 딕셔너리와 for문
my_dic = {
    "name": "이무기",
    "address": "부산 중구",
    "gender": "여자",
    "hobby": ["독서", "음주가무", "강아지 만지기"],
}

# key 값만 순회하는 것, dic에 대해서는 key만 들어가요
for i in my_dic :
    print(i, end = " ")    #end 그냥 두면 줄바뀜이 default
print()

for i in my_dic.keys():
    print(i, end = " ")
print()

print(my_dic.values())
for i in my_dic.values():
    print(i, end = " ")
print()

# key, value 함께 순회하고 싶다?
for key, value in my_dic.items():
    print(f"{key}: {value}", end = " ")
print()