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