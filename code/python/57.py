import matplotlib.pyplot as plt

''' 히스토그램 '''
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


