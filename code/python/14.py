# 이중 for문
for i in range(5) :
    print(f"외부 반목문의 i값 : {i}")

    for j in range(3):
        print(f"내부 반복문의 j값 : {j}")

        print("------------------------")

# 이차원 리스트와 이중 for문
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#요소 (elem 변수)의 합계 구하기
total_sum = 0

for row in matrix :
    #print(f"외부반복문의 row값 : {row}")
    for elem in row:
        #print(f"내부반복문의 row값 : {row}")
        total_sum += elem
    # 1번 시점 : 내부 반복문이 종료될 때
    # print(f"중간합계: {total_sum}")
#2번시점: 외부 반복문이 종료될 때
print(f"전체 합계: {total_sum}")

# 짝수만 출력하기
matrix2 = [
    [1,2,4],
    [44, 55, 77],
    [2, 9, 10]
]
print("짝수만 출력: ", end= " ")
for row in matrix2:
    for elem in row:
        if elem % 2 == 0:
            print(elem, end = " ")

# 구구단 실습
for i in range(2, 10):
    print(f"[{i}단]")
    for j in range(1, 10) :
        print(f"{i} x {j} = {i*j}")
    print() # 이미 한 줄 띄어주는 기능이 있는데 한 줄 띄워주는 기능에 "\n"을써버러니까 두줄이 띄워지는 거임

for i in range(3): #세로
    print("*"*5,end="\n")

for i in range(3): #세로
    print("") #줄바꿈
    for j in range(5): #가로
        print("*", end = "")

#사용자가 입력한 숫자값만큼 입력되도 재밋을 거 같다는데
