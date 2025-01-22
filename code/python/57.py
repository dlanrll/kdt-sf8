import matplotlib.pyplot as plt
"""
data = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5 , 6, 6, 6, 6, 6, 6 , 6 , 6, 6, 6]

plt.hist(data, bins = 11, color ="green", histtype="step")

plt.title("hist")
plt.xlabel("value")
plt.ylabel("bins")
plt.show()

data1 = [1, 2, 2, 3, 3, 3, 4]
data2 = [2, 3, 3, 4, 4, 5, 6]

plt.hist([data1, data2], bins = 5, color = ["green", "purple"], label = ["data1", "data2"])
plt.title("I wanna go home")
plt.xlabel("value")
plt.ylabel("bins")
plt.legend()
plt.show()

''' 산점도 '''
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, , 7, 11]
sizes = [20, 50, 80, 100, 200]
colors = [10, 20, 30, 40, 50]

plt.scatter(x, y, s = sizes, c = colors, cmap = "plasma")
plt.colorbar(label = "color bar")

plt.show()




# 파이차트

# sizes = [25, 25, 20, 20]
# labels = ["A","B", "C", "D"]

sizes = [15, 30,34, 10]
labels = ["apple","banana", "grape", "cherry"]
explode = [0, 0.1, 0, 0]

plt.pie(sizes, labels = labels, explode=explode, autopct = "%1.1f")
plt.show()





import matplotlib.pyplot as plt

# 데이터 설정
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

# 그래프 생성
plt.plot(months, sales_2019, label='2019', marker='o')  # 2019년 데이터
plt.plot(months, sales_2020, label='2020', marker='o')  # 2020년 데이터

# 그래프 제목 및 라벨
plt.title('Monthly Sales Comparison (2019-2020)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()  # 범례 추가

# 그래프 표시
plt.show()
"""


import matplotlib.pyplot as plt

labels = [ 'Banana','Melon', 'Grape', 'Apple']
sizes = [32, 16, 18, 34]
colors = ['yellow','green', 'purple', 'red']  
explode = (0.1, 0, 0.05, 0.05)  

plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    wedgeprops={'width': 0.6, 'edgecolor': 'black'} 
)

plt.show()
