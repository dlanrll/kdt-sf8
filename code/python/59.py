import matplotlib.pyplot as plt
import seaborn as sns

# 데이터셋 
print(sns.get_dataset_names())

# 예제데이터
tips = sns.load_dataset("tips")
# print(tips.info(0))

sns.scatterplot(x='total_bill', y = "tip", data = tips, hue = "size", palette="deep", style = "time", size = "size")


sns.catplot( x = "day", y = "total_bill", data = tips, )
sns.pairplot(data = tips, hue = "time")
sns.regplot(data=tips, x = "total_bill", y = "tips", hue = "time")
