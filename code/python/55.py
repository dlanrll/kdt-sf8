### 실습, 공공데이터 활용

import pandas as pd
file_name = "서울특별시_공원 내 운동기구 설치 현황_20201231.csv"
df = pd.read_csv(file_name, encoding = "cp949")

print(df.head())
df.info()

