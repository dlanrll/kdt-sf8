#song = input("네 최애 축구 선수는 누구니?")
#print(song) #박민서
#print(type(song))

#a = input("1 + 1 = ?")
#print(a)
#print(a*3)

#형변환
# 1. 정수형으로 변환
print(int("10")) #문자열 "10"을 정수로 변환
print(int(10.9)) #실수 10.9를 정수로 변환 (소수점 이하 반환)

# 2. 실수형으로 변환
print(float("11.2"), type(float("11.2"))) #문자열 "11.2"를 실수로 변환
print(float(10), type(float(10))) # 정수 10을 실수로 변환

# 3. 형변환 안 되는 예시
#print(int("name"))
print(int("11.2"))

b = 2 #정수형
print(b*10) #20
print(str(b)*10) #"2"*10 > 2222222222
print(str(b)+"입니다")
print(b + "입니다") #type error 더하기는 문자열끼리 하던지, 숫자끼리 하던지 해야한다!


#str은 숫자값을 문자값으로 바꿔주는 함수임
#str()활용예시
math_score = 80
eng_score = 85
total_score = math_score + eng_score
avg_score = total_score/2
print("합계: ", str(total_score))
print("평균: " + str(avg_score))
print("합계 :", total_score)
print("평균 :", avg_score)


# 1번
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
print(f"안녕하세요! {name}님 ({age}세)")

# 2번
name = input("이름을 입력하세요: ")
birth_year = int(input("태어난 년도를 입력하세요: "))
current_year = int(input("올해 년도를 입력하세요: "))
age = current_year - birth_year
print(f"올해는 {current_year}년, {name}님의 나이는 {age}세 입니다.")
