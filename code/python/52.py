import numpy as np

# 1차원
a1 = np.array([1, 2, 3, 4, 5])
print(a1)

# 2차원
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2)

# 3차원
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a3)

# 배열 모양
print(a2.shape) # (2, 3) > 2에서 3열이라는 뜻
print(a2.ndim)  # 차원을 나타냄, 2 라는 값 반환
print(a2.dtype) # 원소의 자료형 int64, int는 정수를 나타내고 64는 비트의 갯수 아닐까여
print(a2.itemsize) # 각 원소의 크기 byte 단위로 나온다
print(a2.size)  # 원소의 갯수 반환

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 1])
print(arr[2, 2])
row = [0, 2]
col = [2, 2]
print(arr[row, col])

arr =  np.array([10, 20, 30, 40, 50])
print(arr[arr > 20])
print(arr[arr % 20 == 0])
arr[arr > 20] = 0
print(arr)
lists = [2, 3, 4]
print(arr[lists])


# 배열생성
zero = np.zeros((3, 5))
print(zero)
ones = np.ones((5, 5))
print(ones)
ranges = np.arange(1, 20, 3)
print(ranges)
linespaces = np.linspace(0, 2, 10) # 1부터 2까지 10개의 값이 나오도록, 숫자를 균등하게 쪼개어 계산
print(linespaces)

# 1차원 배열을 2X3 배열로 변환
array = np.array([1, 2, 3, 4, 5, 6])
reshaped = np.reshape(array, (2, 3))
print(reshaped)


# 연산
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a+b)
print(a*b)

c = np.array([1, 4, 9, 16, 25, 36])
print(np.sqrt(c))  # 제곱근
print(np.exp(c))   # 지수함수
print(np.log(c))   # 자연로그

angles = np.array([0, np.pi / 6, np.pi / 4, np.pi])
#0, 30, 15, 60, 90
print(angles)
print(np.sin(angles))
print(np.cos(angles))

# 합치기
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 수평합치기
print(np.hstack((a,b)))
# 수직합치기
print(np.vstack(a, b))
# 열기준 합치기
print(np.column_stack((a, b)))

# 분할하기
a = np.array([1, 2, 3], [4, 5, 6])
# 수평분할
h = np.hsplit(a, 3)
print(h)

