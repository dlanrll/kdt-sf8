import pandas as pd


"""
# 리스트형식으로 생성
data = [10, 20, 30, 40]
# series = pd.Series(data) #기본인덱스
series = pd.Series(data, index=["a", "b", "c", "d"])  # 커스텀 인덱스
print(series)

# 딕셔너리형식으로 생성
data = {"a": 10, "b": True, "c": 3.14, "d": "Python"}
series = pd.Series(data, name="딕셔너리")
print(series)
print(series.index)
print(series.values)
print(series.shape)


data = ("민지", "여", False)
member = pd.Series(data, index=["이름", "성별", "결혼여부"])
print(member)
print(member["이름"])
print(member[["성별", "결혼여부"]])


data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
# print(series["a"]) #인덱스를 변경했으면 그 인덱스를 사용(권장)
print(series[series > 20])
series["c"] = 100
print(series)
print("a" in series)  # 인덱스 "a"가 존재
print(series.sum())  # 합계
print(series.mean())  # 평균
print(series.max())  # 최대값
print(series.astype(float))  # 타입을 변경


# pandas vs numpy
# 인덱스: 커스텀가능 vs 숫자(0부터)
# 데이터타입 : 혼합가능 vs 단일


# 실습1. 시리즈만들기
data = ["4 cups", "1 cup", "2 large", "1 can"]
index = ["밀가루", "우유", "계란", "참치캔"]
series = pd.Series(data, index=index, name="Dinner")
print(series)

# --------------------------------------------------------
# 데이터프레임
index = ["2020", "2021", "2022", "2023", "2024", "2025"]
yeonghee = pd.Series([140, 150, 160, 170, 180, 190], index=index)
cheolsu = pd.Series([200, 210, 220, 230, 240, 250], index=index)

result = pd.DataFrame({"영희": yeonghee, "철수": cheolsu})
# print(result)
# print(result.head())  # 위에서부터 기본5개보여줌
# print(result.tail()) # 아래서부터 기본5개
# print(result.shape) # 데이터크기(행, 열)
# print(result.info())  # 요약정보
# print(result.columns)  # 열이름
# print(result.values) #행값
# print(result.index) #인덱스값
# print(result.dtypes)
# print(result["철수"])
# print(result[["철수"]])
"""

data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, 30, 27],
    "City": ["서울", "부산", "인천"],
}
df = pd.DataFrame(data, index=["a", "b", "c"])
# print(df)
# 데이터값 추출하는 방법########
# loc(index, column)
# print(df.loc["b"])
# print(df.loc["b", "Age"])
# print(df.loc["a":"c", "Name":"Age"])
# print(df.loc[~(df["Age"] >= 30)])
# print(df.loc[:, "Name"])
# print(df.loc["a", :])

# print(df.iloc[1])
# print(df.iloc[1, 1])
# print(df.iloc[0:2, 0:1])  # 끝값이 포함되지 않음
# print(df.iloc[[0, 2], [1, 2]])
# print(df.iloc[:, 0])
# print(df.iloc[0, :])
#############################

# 데이터를 넣고 추가/수정하는 방법#########
# 행추가
# new_data = {"Name": "이몽룡", "Age": 31, "City": "포항"}
# result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
# print(result)

# 인덱스와같이 행추가
new_data = pd.DataFrame({"Name": "이몽룡", "Age": 31, "City": "포항"}, index=["d"])
# concat
result = pd.concat([df, new_data])
# loc
result.loc["e"] = ["전우치", 28, "대전"]
# print(result)

# 열추가
result["직업"] = ["엔지니어", "개발자", "디자이너", "기획자", "데이터분석가"]
# print(result)

# 요소값수정
result.at["b", "City"] = "천안"
result.loc[result["Name"] == "임꺽정", "Age"] = 31
print(result)

# 컬럼값 변경
result.rename(columns={"Name": "이름", "Age":"나이", "City" :"도시"}, inplace = True)
print(result)
inplace = True : 원본 데이터 수정

# 데이터 정렬(기본: 오름차순)
result.sort_values(by = "나이", inplace=True, ascending=False)  # ascending = False 내림차순
print(result)


# 컬럼 삭제







import pandas as pd

# 초기 데이터 생성
data = {
    "이름": ["홍길동", "임꺽정", "성춘향"],
    "수학": [85, 90, 78],
    "영어": [88, 76, 92],
    "과학": [95, 89, 84]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 열 이름 변경 (수학 -> Math)
df.rename(columns={"수학": "Math"}, inplace=True)

# 총점 계산 후 열 추가
df["Total"] = df["Math"] + df["영어"] + df["과학"]

# 새로운 행 추가
new_row = {"이름": "이몽룡", "Math": 88, "영어": 85, "과학": 90, "Total": 88 + 85 + 90}
df = df.append(new_row, ignore_index=True)

# 출력
print(df)
