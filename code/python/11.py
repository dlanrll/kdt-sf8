# while문
i = 5
while i > 0 :
    print("반복문 연습", i)
    i -= 1

print("종료")

# 합계 구하기
num = 1 #더하는 숫자
total = 0 # 총합
while num <= 10 :
    total += num # total = total + num
    print("현재 total 값 >", total)
    num += 1 

print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료" :
    user_input = input("원하는 값을 입력하세요. '종료' 입력시 종료됩니다.")
    print(f"입력한 값 : {user_input}")

print("프로그램이 종료되었습니다.")

# ctrl + C = 무한루프에사 빠져나오는 법~!

#break 문
# 예시. 숫자를 입력받아서 0이 입력되면 반복문 종료
while True : 
    num = int(input("숫자 입력(0 입력시종료):"))

    if num == 0 :
        print("프로그램 종료")
        break

    print(f"입력한 숫자는 {num}입니다.")


# continue 문
# 예시. 숫자 입력받고 짝수만 출력하고 홀수는 건너뛰기
while True :
    num = int(input("숫자 입력(음수 입력시 종료) : "))

    if num < 0 :
        print("프로그램 종료")
        break

    if num % 2 != 0:
        continue # 홀수 건너뛰고, 다시 입력받기

    print(f"입력한 짝수는 {num}입니다.")


# 실습 While문 사용하기
# 사용자에게 숫자를 입력받아, 그 숫자가 양수일 경우 1부터 해당 숫자까지의 합을 계산하고 출력하는 프로그램을 작성하시오
while True:
    user_input = input("숫자를 입력하세요 (종료를 원하면 '종료'를 입력): ")

    if user_input == "종료":
        print("프로그램을 종료합니다.")
        break

    if not user_input.isdigit():  #0부터 9까지만 인식함
        print("양수만 입력하세요.")
        continue

    number = int(user_input)
    if number == 0:
        continue

    total_sum = sum(range(1, number + 1))
    print(f"1부터 {number}까지의 합은 {total_sum}입니다.")

'''total = 0
    num = 1
    while num <= number:
        total += num
        num += 1
    print(f"1부터 {number}까지의 합은 {total}입니다.")

# 무한루프를 예방하기 위하여 종료 세션이 들어간 코드는 제일 앞에 작성하고, 가장 중요한 코드는 제일 마지막에 작성함
'''

'''
input은 기본적으로 문자열을 받잖아, 근데 거기까지는 괜찮은데음
isdigit이 0-9의 아라비아 숫자를 나타냄 그러니까 문자나 마이너스 부호같은 경우에는 인식을 못함
여튼... number에 이제 숫자를 넣을 거니까 int로 선언을 해주고! total의 sum을 구한다
나는 그냥 range함수를 써서 전체의 값을 구했는데 사람들은 sum += i 를 쓰는데 사실 나는 이게 더 이해가 안 간다... 하

이 실습 중 가장 깔끔하다고 생각한 코드 (수빈님)
while True:
    user_input = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료): ")
    sum = 0
    i = 0
    if user_input == '종료':
        print("프로그램을 종료합니다.")
        break
    elif user_input > '0' and user_input.isdigit() == True:
        while i <= int(user_input):    
            sum += i
            i += 1
        print(f"1부터 {int(user_input)}까지의 합은 {sum}입니다.")
    elif user_input == '0':
        continue
    elif user_input < '0' or user_input.isdigit() == False: 
        print("양수만 입력 하세요.")
        continue
    '''

''' 아이고 강사님 코드
while True:
    positive_input = input("양수를 입력하세여 ('종료' 입력시 프로그램 종료): ")
    
    if positive_input == "종료":
        print("프로그램을 종료 합니다")
        break
    
    try: 
        positive_input = int(positive_input)
        
        if positive_input < 0:
            print("양수만 입력하세여")
            continue
        elif positive_input == 0:
            continue
        else:
            result = 0
            i = 1
            
            while i <= positive_input:
                result = result + i
                i = i + 1
                
            print(f"1부터 {positive_input}의 합은 {result}입니다")

    
    except:
        print("양수만 입력하세여")
        continue
'''