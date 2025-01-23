import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = "Pretendard-Medium.ttf"  # 폰트 파일 경로
font_prop = font_manager.FontProperties(fname=font_path)
# 한국어 쓰고 마지막에 이거 넣기 fontproperties=font_prop

file_name = "연령별인구현황_월간.csv"
data = pd.read_csv(file_name, encoding = "EUC-KR")
# data.info()

region_name = input("검색하고 싶은 지역명을 입력하새요. : ")

# 우리가 원하는 나이 컬럼 리스트, 세만 붙어있는 컬럼들만 리스트로 다시 뽑아냄
age_columns = [ col for col in data.columns if "세" in col ]    # if "A" in col 이렇게 하면 col안에 뭐가 있다면, 그것만 출력해라는 뜻
# print(age_columns)

# 숫자로 변환
for col in age_columns:
    data[col] = data[col].str.replace(",","").astype(int)

# 필터링
# contains(): 문자열 데이터 필터링, 특정 패턴을 찾을 때
# 옵션값
# na : 결측값을 포함할지 결정, 기본값 True
# case : 영문의 대소문자를 구분, 기본값 True

region_data = data[data["행정구역"].str.contains(region_name, na = False)]

if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")
    exit()

# 데이터 추출
# 2024년12월_계_0~9세 ["2024년12월", 0~9세]
age_groups = [ col.split("_계_")[1] for col in age_columns] 

# 결과값
result = region_data[age_columns].iloc[0].values

# 그래프 그리기
plt.figure(figsize = (10, 8))
plt.plot(age_groups, result, marker = "o", label = region_name)
plt.title(f"{region_name}의 연령별 인구수", fontproperties=font_prop, fontsize = 16, pad = 10)
plt.xlabel("연령대",fontproperties=font_prop)
plt.ylabel("인구수", fontproperties=font_prop)
plt.grid(True, linestyle = "--", alpha = 0.6 )
plt.xticks(rotation = 45)
plt.legend()
plt.show()


''' 연령별 인구 현황 월간 실습 내가 적은 코드 '''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = "Pretendard-Medium.ttf" 
font_prop = font_manager.FontProperties(fname=font_path)

file_path = "연령별인구현황_월간_실습.csv"
data = pd.read_csv(file_path, encoding="EUC-KR", thousands=",") # thousands = 숫자 구분자를 자동으로 인식하고 제거하는 파라미터, 판다스 데이터프레임을 읽을 때 사용

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

    plt.figure(figsize=(12, 8))
    plt.plot(age_groups, male_data, marker="o", label="남성", color="blue")
    plt.plot(age_groups, female_data, marker="o", label="여성", color="red")
    plt.title(f"{region_name}의 연령별 인구수", fontproperties=font_prop, fontsize=16, pad=10)
    plt.xlabel("연령대", fontproperties=font_prop)
    plt.ylabel("인구수", fontproperties=font_prop)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.legend(prop=font_prop)
    plt.show()
