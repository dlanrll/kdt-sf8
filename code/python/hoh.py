import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = "Pretendard-Medium.ttf" 
font_prop = font_manager.FontProperties(fname=font_path)

file_path = "연령별인구현황_월간_실습.csv"
data = pd.read_csv(file_path, encoding="EUC-KR", thousands=",")
# thousands = 숫자 구분자를 자동으로 인식하고 제거하는 파라미터, 판다스 데이터프레임을 읽을 때 사용
# 쉼표는 자동으로 제거되고 데이터가 숫자(int 또는 float) 형식으로 불러와진다

region_name = input("검색하고 싶은 지역명을 입력하새요. : ")

region_data = data[data["행정구역"].str.contains(region_name, na=False)]

if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")
    exit()
else:
    male_columns = [col for col in data.columns if "세" in col and "남" in col]
    female_columns = [col for col in data.columns if"세" in col and "여" in col]

    male_data = region_data[male_columns].iloc[0].values
    female_data = region_data[female_columns].iloc[0].values

    age_groups = [col.split("_")[-1] for col in male_columns]

    plt.figure(figsize=(10,6))
    plt.plot(age_groups, male_data, marker="o", label="남성", color="blue")
    plt.plot(age_groups, female_data, marker="o", label="여성", color="red")
    plt.title(f"{region_name}의 연령별 인구수", fontproperties=font_prop, fontsize=16, pad=10)
    plt.xlabel("연령대", fontproperties=font_prop)
    plt.ylabel("인구수", fontproperties=font_prop)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.legend(prop=font_prop)   # 그래프의 범례를 지정, 범례의 스타일을 지정하는 코드
    plt.show()