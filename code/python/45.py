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

# with open("user.txt", "r", encoding="utf-8") as file:
#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()

# str = "                    문자열                        "
# print(f"[{str.strip()}]")  # 양쪽공백제거
# print(f"[{str.rstrip()}]")  # 우측공백제거
# print(f"[{str.lstrip()}]")  # 좌측공백제거


# enumerate() # 리스트를 튜플형태로 반환, 반환값이 두개
with open("user.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    # (0, "동해물과\n"), (1, "백두산이\n") <= ["동해물과\n", "백두산이\n"]
    for idx, value in enumerate(lines):
        print(f"{idx}인덱스의 값은 {value.strip()}입니다.")

# ==================바이너리 파일=======================
# with open("owl.png", "rb") as file:
#     # data = file.read()
#     # print(f"{len(data)} 바이트")
#     header = file.read(10) # 파일확장자를 찾는 방법
#     print(f"{header}")


def files(file_path):
    with open(file_path, "rb") as file:
        header = file.read(4)  # 4바이트가 확장자의 매직넘버
        # print(header)
        if header == b"\x89PNG":  # png는 첫 4바이트가 89 50 4e 47
            return "png"
        elif header[:2] == b"\xff\xd8":  # jpg는 2바이트이때문에 뒤에 2바이트를 삭제
            return "jpg"
        else:
            return "unknown"


print(files("owl.png"))

# # 바이너리파일 쓰기
# with open("owl.png", "rb") as file:
#     data = file.read()

# with open("owl_copy.png", "wb") as file:
#     file.write(data)


