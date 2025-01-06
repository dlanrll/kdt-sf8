# 이차원 리스트
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
print(matrix)

print(matrix[0])  # 첫번째 행
print(matrix[1])  # 두번째 행
print(matrix[2])  # 세번째 행

print(matrix[0][0])  
print(matrix[1][2])  

# 요소 추가
matrix[1] = matrix[1] + [99] 
print(matrix)

# 행 추가
matrix = matrix + [[10, 11, 12]]
print(matrix)

# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 5000
print(matrix)

# 행 삭제
del matrix[2]
print(matrix)

# 행 개수
rows = len(matrix)
print(rows)

# 열 개수
rows2 = len(matrix[0])
rows3 = len(matrix[1])
rows4 = len(matrix[2])
print(rows2) # 3
print(rows3) # 4
print(rows4) # 3


# 이차원 매서드
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 요소추가
matrix[0].append(10)
print(matrix)

# 행추가
matrix.append([10, 11,12])
print(matrix)

matrix[1].insert(1, 100)
print(matrix)

#요소 삽입
matrix[1].insert(1, 100)
print(matrix)

# 행삽입
matrix.insert(2, ["안녕","반가워","어서와"])
print(matrix)

# 리스트 확장
matrix[0].extend([11, 12])
print(matrix)

# 아이스크림 문자열 만들기
words = [
    [["마", "크"], ["구", "이"]],
    [["피", "아"], ["림", "차"]],
    [["스", "사"], ["나", "가"]],
]
print(words[1][0][1] + words[0][1][1] + words[2][0][0] + words[0][0][1] + words[1][1][0])


'''불변 (immutable) -> 변경할 수 없는
불변 객체 -> 한 번 생성된 객체의 상태를 변경할 수 없다.'''

# 튜플, Tuple
t1 = (1, ) #요소가 1개인 튜플은 반드시 쉼표 사용!
print(t1)

not_tuple = (1)
print(not_tuple)

t2 = (1, 2, 3, 4, 5, 3, 3, 3,)
print(t2)

t3 = 1, 2, 3
print(t3)

t4 = ("a", "b", "c", ("안녕", "감자"))
print(t4)

print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(t4[:2])

print("a" in t4)
print("d" in t4)

t4[0] = "x"