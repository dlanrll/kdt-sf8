### 실습, 공공데이터 활용

import pandas as pd
file_name = "서울특별시_공원 내 운동기구 설치 현황_20201231.csv"
df = pd.read_csv(file_name, encoding = "cp949")

df.columns = df.columns.str.strip() 
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 1. 공원별 총 운동기구 설치 수
result_park = df.groupby("구분")["운동기구 수량"].sum()
with open("공원별_총_운동기구_설치_수.csv", "w", encoding="utf-8") as file:
    result_park.to_csv(file, header=True)

# 2. 운동기구 종류별 설치 개수
result_equipment = df.groupby("운동기구 기종명")["운동기구 수량"].sum()
print("2. 운동기구 종류별 설치 개수")
print(result_equipment)
print()

# 3. 관리기관별 총 운동기구 설치 수
result_institution = df.groupby("관리기관")["운동기구 수량"].sum()
print("3. 관리기관별 총 운동기구 설치 수")
print(result_institution)
print()

# 4. 특정 공원 데이터 필터링
park_name = "한강공원(잠실지구)"
filtered_park = df[df["구분"].str.strip() == park_name]
print(f"4. 특정 공원 데이터 필터링 (공원 이름: {park_name})")
print(filtered_park)
print()

# 5. 특정 운동기구 종류 데이터 필터링
equipment_name = "벤치프레스"
filtered_equipment = df[df["운동기구 기종명"].str.strip() == equipment_name]
print(f"5. 특정 운동기구 종류 데이터 필터링 (운동기구: {equipment_name})")
print(filtered_equipment)
print()

# 6. 운동기구 수량 기준 내림차순 정렬
sorted_equipment = df.sort_values(by="운동기구 수량", ascending=False)
print("6. 운동기구 수량 기준 내림차순 정렬")
print(sorted_equipment)