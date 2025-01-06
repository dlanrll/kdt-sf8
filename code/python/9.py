# 내장함수
# max() : 최대값을 반환하는 함수
# min() : 최소값을 반환하는 함수

numbers = [10, 20, 30, 40]
print(sum(numbers))

scores = {"국어" : 83, "영어" : 90, "수학" : 95}
print(scores.values())
total_score = sum(scores.values())
print(total_score)

print(max(numbers))
print(min(numbers))

print(max(scores.values()))
print(min(scores.values()))

names = ["Alice", "Bob","Charlie"]
scores = [85, 90, 95]
zipped = list(zip(names, scores))
print(zipped)

