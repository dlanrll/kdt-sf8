import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
'''
penguins = sns.load_dataset("penguins")

# 1. 종(species)별 평균 몸무게(body_mass_g), bar
plt.figure(figsize=(8, 6))
sns.barplot(x="species", y="body_mass_g", data=penguins, palette="pastel")
plt.show()

# 2. 부리 길이(bill_length_mm)와 부리 깊이(bill_depth_mm)의 관계, scatterplot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x="bill_length_mm", y="bill_depth_mm", hue="species", data=penguins, palette="pastel"
)
plt.show()

# 3. 섬(island)에 따른 몸무게 분포, violinplot
plt.figure(figsize=(8, 6))
sns.violinplot(x="island", y="body_mass_g", data=penguins, palette="pastel")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# flights 데이터셋 로드
flights = sns.load_dataset("flights")

# 1. 연도(year)별 승객 수(passengers)의 평균을, lineplot
year_avg = flights.groupby("year")["passengers"].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.lineplot(x="year", y="passengers", data=year_avg, color="blue")
plt.show()

# 2. 연도와 월별 승객 수, heatmap
flights_pivot = flights.pivot(index = "month", columns = "year", values = "passengers")
plt.figure(figsize=(10, 8))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="coolwarm", cbar=True)
plt.show()

# 3. 특정 연도(1958년)의 월별 승객 수, barplot
flight1958 = flights[flights["year"] == 1958]
sns.barplot(data=flight1958, x="month", y="passengers")
plt.show()
'''




import seaborn as sns
import matplotlib.pyplot as plt

# titanic 데이터셋 로드
titanic = sns.load_dataset("titanic")

# 1. 탑승 클래스(class)와 생존 여부(survived)의 관계를 catplot으로 시각화
sns.catplot(data=titanic, x="class", hue="survived", kind="count")
plt.show()

# 2
plt.figure(figsize=(10, 6))
sns.kdeplot(data=titanic, x="age", hue="survived")
plt.show()
