#한 줄 주석(ctrl+/ = 주석단축키)
#ctrl + F5 전체 실행, shift + enter 한 줄만 실행

'''
여기는 여러줄
주석을 나타낸다
'''

"""
쌍따옴표
세개도 가능함
"""

print("hello, world")

print("hello", "world")
print("hello","world", sep="")  #sep = seperate 구분자
print("010", "1234", "5678", sep="-")
print("hello", "python", 1, 2,sep = "-") #자료형, 문자열과 숫자열 각 데이터자료가 다른 문장이 같이 있음
print() #print 함수 안에 아무것도 안 넣으면 줄 바뀜
print("111")

print("안녕하세요, ", end="") #end옵션: 문장 끝에 넣고싶은 것 넣고 한 줄로 연결
print("채연이에요")

ive = "I AM"
print(ive)
ive = "장원영"
print(ive)
print(f"제가 좋아하는 가수는 {ive}입니다.") #문자열 포매팅
print("제가 제일 좋아하는 가수는", ive, "입니다.", sep=" ") #위와 결과 동일


