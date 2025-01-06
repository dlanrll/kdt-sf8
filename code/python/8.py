# 딕셔너리

# 빈 딕셔너리 생성
dict1 = {}
dict1 = dict()
print(dict1)

# 딕셔너리 생성
dict1 = {
    "name" : "홍길동",
    "age" : 20,
    "city" : "Seoul",
    "hobby": ["런닝", "등산", "헬스"]
}
print(dict1)

dict2 = dict(name = "홍길동", age = "21")
print(dict2)

# 값 접근하기
print(dict1['name'])
print(dict1["hobby"])
print(dict1["hobby"][2])

# 값 수정
dict1["age"] = 30
print(dict1)

# 요소 추가
dict1["birthday"] = "20020520"
print(dict1)

# 키 삭제
del dict1["birthday"]
print(dict1)

# 딕셔너리 메서드
fruits = {"apple" : "사과", "banana" : "바나나"}
print(fruits.get("apple"))
print(fruits.get("peach"))
#존재하지 않는 키로 get 하는 경우 "None" 반환
print(fruits.get("peach", "복숭아"))
# > 존재하지 않는 키로 검색시 기본값 설정
print(fruits)
# 기본값을 설정할 뿐, 딕셔너리 추가 요소는 아니다

# 여러 요소 추가
fruits.update({"grape" : "포도", "melon" : "멜론"})
print(fruits)
print(fruits.keys())
print(fruits.values())
print(fruits.items())

# 요소 모두 지우기
fruits.clear()
print(fruits)




students_scores = {}

students_scores["Alice"] = 85
students_scores["Bob"] = 90
students_scores["Charlie"] = 95

students_scores["David"] = 80

students_scores["Alice"] = 88

del students_scores["Bob"]

# 최종 결과 출력 (테스트용)
print(students_scores)

