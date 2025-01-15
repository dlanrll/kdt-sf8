# 파일 입출력
# 파일 쓰기
# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("안녕하세요\n")
#     file.write("파이썬파일쓰기연습\n")

# 내용추가
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("내용추가\n")
#     file.write("11111")

# writelines()
# lines = ["첫번째내용\n", "두번째내용\n", "세번째내용\n"]

# with open("test2.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)

# # 사용자로부터 입력받은 내용을 파일로 만들기
# with open("user.txt", "w", encoding="utf-8") as file:
#     while True:
#         line = input("파일에 넣을 문자열입력(종료하려면 '종료'입력)")
#         if line == "종료":
#             print("\n입력을 종료합니다")
#             break

#         file.write(line + "\n")


# 파일 읽기
# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.read())  # 파일 전체읽기

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readline()) # 파일 한줄씩 읽기
#     print(file.readline())

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readlines()) # 파일을 리스트형태로 반환

with open("user.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# str = "                    문자열                        "
# print(f"[{str.strip()}]")  # 양쪽공백제거
# print(f"[{str.rstrip()}]")  # 우측공백제거
# print(f"[{str.lstrip()}]")  # 좌측공백제거

