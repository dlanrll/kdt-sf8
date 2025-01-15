import random
import time

# 단어 리스트
words = ["sunlight", "cloud", "rainbow", "moonlight", "thunder", "star", "comet", "planet", "galaxy", "universe"]

def typing_game():
    print("\n영어 타자 연습 게임을 시작합니다! 'exit'을 입력하면 종료됩니다.")
    random.shuffle(words)  # 단어 랜덤 순서로 섞기
    correct_count = 0
    total_time = 0

    for word in words:
        start_time = time.time()  # 단어 시작 시간 기록
        print(f"\n단어: {word}")

        while True:
            user_input = input("입력: ")

            if user_input == "exit": # 게임 종료
                average_time = total_time / correct_count if correct_count > 0 else 0
                print("\n게임 종료!")
                print(f"총 {correct_count}개의 단어를 입력하셨습니다.")
                print(f"총 걸린 시간: {total_time:.2f}초")
                print(f"평균 단어 입력 시간: {average_time:.2f}초")
                return

            if user_input == word:
                print("통과!")
                correct_count += 1
                end_time = time.time()  # 단어 입력 완료 시간 기록
                total_time += end_time - start_time
                break
            else:
                print("오타! 다시 시도하세요.")

    # 게임 종료 후 결과 출력
    average_time = total_time / correct_count if correct_count > 0 else 0
    print("\n게임 종료!")
    print(f"총 {correct_count}개의 단어를 입력하셨습니다.")
    print(f"총 걸린 시간: {total_time:.2f}초")
    print(f"평균 단어 입력 시간: {average_time:.2f}초")

# 게임 실행
typing_game()



# 영어단어게임 실습 : 강사님 코드
# 실습. 타자연습게임
import random
import time

words = [
    "mountain",
    "river",
    "forest",
    "ocean",
    "desert",
    "tree",
    "flower",
    "cloud",
    "rain",
    "sunlight",
]


def game():
    print("영어 타자 연습 게임")
    print("게임종료를 원하시면 exit를 입력하세요")

    total_words = 0  # 게임한 단어 갯수
    start_time = time.time()  # 게임시작 시간

    while True:
        word = random.choice(words)
        print(f"단어 : {word}")

        while True:
            user_input = input("입력 : ")

            if user_input == "exit":  # 게임 종료
                end_time = time.time()
                total_time = end_time - start_time
                print("\n게임종료")
                print(f"총입력한 단어는 {total_words}개 입니다.")
                print(f"총걸린시간은 {total_time:.2f}초")
                print(f"단어당 평균시간은 {total_time / total_words:.2f}초")
                return

            if user_input == word:
                print("통과!")
                total_words += 1
                break
            else:
                print("오타! 다시입력하세요")


game()
