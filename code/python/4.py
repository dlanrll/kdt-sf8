number = [1,2,3, "hello", "python"]
print(number)

# 인덱싱 (indexing) : 인덱스 번호로 요소를 추출하는 것
print(number[3]) #hello만 잡힌다, 즉 대괄호 안 숫자 n+1 번째의 값을 출력함
print(number[0]) #인덱스의 번호는 0부터 시작한다
#print(number[100]) #범위를 벗어난 인덱스 번호

#list() 함수: 리스트를 생성하는 내장함수 (반복 가능한 객체를 리스트로 변환할 때 사용
# 반복 가능한 객체? : 문자열, 튜플, 셋(집합), 딕셔너리, 또 다른 리스트
text = "hello, python"
print(list(text))  #print 값 : ['h', 'e', 'l', 'l', 'o', ',', ' ', 'p', 'y', 't', 'h', 'o', 'n']

invalid = 1234
print(list(invalid)) # TypeError: 'int' object is not iterable = 정수는 반복 가능한 객체가 아님

shop = ['반팔', '청바지', '이어폰', '키보드']

# 인덱싱
print(shop[0]) #반팔

# 슬라이싱
print(shop[0:2])  # ['반팔', '청바지'] 0 < = shop < 2

# 리스트 안에서 리스트 인덱싱
# 이부분 다시 ppt보고 하기

print(text[7]+text[8]+text[9]+text[10]+text[11]+text[12])
print(text[7:])

#퀴즈, 문자열 슬라이싱
date = "20250106"
year = date[0:4]
month = date[4:6]
day = date[6:]
print(year + "년" + month + "월" + day + "일" )

# 문자열에서 사용 가능한 함수
print(len(date)) # len() : 문자열의 길이를 구하는 함수
print(len(text))
print(text.count("p")) # count() : 해당 문자열 내에서 특정 부분 문자열이 등장한 횟수를 구하는 함수, 대소문자 구별함


# 리스트 슬라이싱
shop = ["반팔", "청바지", "이어폰", ["무선크보드", "기계식키보드"]]
print(shop[:2]) # 0 < = shop , 2
print(shop[3])
print(shop[-2]) # 음수 인덱싱 가능 (뒤에서부터 카운틴 -1부터 시작)
print(shop[:]) #처음부터 끝까지 다 나옴

# 리스트 수정
shop[0] = "긴팔" # 반팔이 긴팔로 수정 됨
print(shop)
shop[100] = "신발" # 존재하는 범위 내에서만 수정할 수 있음

# 리스트 삭제
del shop[1]
print(shop)
print(shop[1])

del shop[2:]
print(shop)  # 복수삭제

# 리스트 연산
a = [1, 2, 3]
b = ["안녕", "반가워"]
print(a+b) # 이어쓰기
print(b*3) # 반복하기


# sorted() : 오름차순 정렬 함수, 원본 리스트는 그대로고 새로운 리스트가 반환, 문자(사전순서)와 숫자 둘 다 가능
# sort() : 오름차순 정렬, 원본 리스트가 변화
# reverse() : 인덱스의 요소를 역순으로 정렬, 값에 대한 내림차순이 아니라 진짜 그인덱스 순서를 반대로 뒤집는 거임
# 숫자열 문자열 마찬가지

#정렬 함수
# asc : ascending (오름차순)
# desc : descending (내림차순)
num = [3, 1, 5, 2]
num_asc = sorted(num)
print(num)
print(num_asc)

num_desc = sorted(num, reverse=True)
print(num_desc)

num.sort() # 매서드
print(num)

''' 함수 vs 매서드
함수 :  어떤 입력값이든 사용 가능한 도구 (전역적)
     ex) sorted() : 리스트 뿐만 아니라 iterable 객체에서 사용 가능
메서드 : 특정 객체의 동작 (종속됨)
       ex) sort() : 리스트 객체에 종속된 메서드 '''

korean = ["강", "이", "박", "최", "김"]
korean.sort(reverse=True)
print(korean)

alphabet = ["b", "c", "a", "d"]
alphabet.reverse() # 내림차순이 아니라 인덱스 역순
print(alphabet)
# 새로운 리스트 반환하지 않고 원본 리스트를 변경

print(alphabet.index("c"))

# 요소 추가, 삭제, 삽입
a = ["a", "b", "c", "안녕", "hi"]
print(a)

a.append("Good")
print(a)

a.pop()
print(a)

a.pop(2)
print(a)

a.remove("안녕")
print(a)

a.insert(2, "잘가")
print(a)

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

# 2번 인덱스 값 출력
print(rainbow[2])
# 알파벳 순서로 정렬한 값 출력
rainbow_desc = sorted(rainbow, reverse=False)
print(rainbow_desc)

rainbow.sort()
print(rainbow)
#좋아하는 색 맨 마지막에 추가하기
rainbow.append("skyblue")
print(rainbow)
#3-6번째 값 삭제하기
del rainbow[2:7]
print(rainbow)

"""이 과제에서 가장 효율적이고 직관적으로 잘 쓴 것 같은 코드
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
# 1. 2번 인덱스 값 출력
print(rainbow.index(2))
# 2. 알파벳 순서로 정렬한 값 출력하기
print(rainbow.sort)
# 3. 좋아하는 색 맨 마지막에 추가하기
rainbow.append("green")
# 4. 3~6번째 값 삭제하기
del rainbow[3:7]
"""