import matplotlib.pyplot as plt
from matplotlib import font_manager
'''
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]


# # 폰트경로
plt.plot(x, y)
font_path = "Pretendard-Medium.ttf"  # 폰트 파일 경로
font_prop = font_manager.FontProperties(fname=font_path)
plt.title("매플롯립", fontproperties=font_prop)


# ------------------------------------------------
# 기본사용법
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# plt.plot(x, y, color="red", linestyle="--", linewidth=3, label="Sample graph") #일반적인선
plt.plot(
    x,
    y,
    marker="*",
    markersize=20,
    markerfacecolor="red",
    markeredgecolor="blue",
    label="marker sample",
)  # 마커표시

font = {
    "size": 20,
    "color": "white",
    "backgroundcolor": "black",
    "weight": "bold",
}  # 폰트설정

# plt.title("Matplotlib", pad=10, fontsize=20, color="white", backgroundcolor="green") # 풀어쓰는방법
plt.title("Matplotlib Dict", pad=10, fontdict=font)  # 딕셔너리 이용방법

plt.legend(title="legend", fontsize=13, loc="lower center")  # 범례표시
plt.grid(True, axis="both", linestyle="--", color="blue", alpha=0.1)  # 그리드

# x,y축 레이블
plt.xlabel("x axis", fontdict=font, labelpad=10)
plt.ylabel("y axis", fontdict=font)

# 축범위설정
plt.xlim([1, 10])
plt.ylim([0, 20])
plt.axis([1, 10, 0, 20])
plt.axis("equal") # x축과 y축을 동일하게 설정
plt.axis("tight") # 그래프가 모든영역을 채우도록 설정
plt.axis("scaled") # 데이터의 비율에 따라서 설정
plt.axis("auto")

plt.show()
'''


''' 하나의 창에 여러개의 그래프 그리기 
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
plt.plot(x, y1, label = "y = x", color = "red")
plt.plot(x, y2, label = "y = x", color = "orange")
plt.plot(x, y3, label = "y = x", color = "green")
plt.plot(x, y4, label = "y = x", color = "blue")

plt.legend(title = "4graph", loc = "upper center", ncol = 4)
plt.title("I wanna go home right now")
plt.xlabel("x")
plt.ylabel("y")
plt.show()'''

''' 하나씩 여러개 그리기 
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title(" x = y ")

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title(" x = y2 ")

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title(" x = y3 ")

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title(" x = y4 ")

plt.show()'''


''' 하나씩 여러개 그리기 방법2 
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, y1)
axes[0, 0].set_title("x = y")

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("x = 2y")

axes[1, 0].plot(x, y3)
axes[1, 0].set_title("x = 3y")

axes[1, 1].plot(x, y4)
axes[1, 1].set_title("x = 4y")

plt.suptitle(" I really wanna go home ")
plt.tight_layout()
plt.show()'''



''' 막대 그래프 '''
categoriese = ["A", "B", "C"]
values = [10, 15, 7]

plt.bar(categoriese, values, width = 0.5, color =["r", "g", "b"], alpha = 0.5, edgecolor = "black", linewidth = 5, align = "edge") # align = dege 하면 x축 표시가 끝부분에 나오는 거임
plt.xticks(categoriese, ["2023", "2024", "2025"])
plt.title("Bar graph")
plt.show()

# 바그래프별 텍스트 넣기
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x좌표(막대의 중심)
        bar.get_height() - 0.5,  # y좌표
        str(bar.get_height()),
        ha="center",
        va="top",
        color="black",
    )

plt.title("Bar graph")
plt.show()


''' 수 평 '''
# 저장
plt.savefig("bar.jpg", format = "jpg")




