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


print(type(77)) #int : 숫자형 중에서 정수의 타입
print(type(7.2)) #float: 숫자형 중에서 실수의 타입
print(type("i\'ve"))
print(type('i\"ve'))
print("i\'ve")
print('i\"ve')

a = 77 
print(type(a))
a = 7.2
print(type(a))
a = 'ive'
print(type(a)) #str: 문자열

print("111\n111") #\n 줄바꿈
print("111\t111") #\n 8칸 띄어쓰기
 

print('''
      |\_/|
      |q p|    /}
      ( w )"""\\
      |"^"`    |
      ||_/=\\__|''')


num = 10  #10진수
b_num = 0b1010 #2진수
h_num = 0xA #16진수
print(num)
print(b_num)
print(h_num)

print(bin(10)) #10진수 to 2진수
print(hex(10)) #10진수to 16진수
print(type(bin(10))) #문자열
print(type(hex(10))) #문자열

print("너무 잠이 솔솔 온당 어쩌지 우뜨카면 좋을까")

print(ord("o")) #ord() : 주어진 문자를 해당하는 유니코드 정수값으로 변환
print(ord("A"))

print(chr(48)) #chr(): 주어진 유니코드 정수값을 문자로 반환
print(chr(65))