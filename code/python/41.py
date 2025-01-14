import sys, os
# 명령어 인수 전체 리스트 출력
'''
print(sys.argv)
print(sys.argv[0])
# print(sys.argv[1])

# python 버전 출력
print(sys.version)

# 프로그램 종료
print("프로그램 종료합니다.")
# sys.exit(0)
# print("이 문장은 실행되지 않는대욬ㅋ")

print()
# 현재 디렉토리 출력
print("현재 작업 디렉토리", os.getcwd())
file_path = os.chdir
'''

# 디렉토리 생성
#os.mkdir("temp")
#print("폴더가 생성됨")

os.rmdir("temp")
print("폴더 삭제됨")

# 환경 변수 출력
# 환경변수 : PATH라는 곳에 경로를 따라 미리 세팅해서 필요에 따라 언제든지 다져다 쓰고자 하는 것
print("PATH 환경변수: ")

"""JSON (JavaScript Object Notaion)
: "JavaScript(언어) Object 자료형과 유사하게 생긴 텍스트 형식"
-> 가독성이 뛰어남 (컴퓨터도 사람도 해석하기 편함)
-> "경량하다는 특성으로 인해" 네트워크를 통해 다른 시스템간 소통할 때 자주 사용
-> JavaScript 언어에서부터 파생되었는데, 현재는 다른 프로그래밍 언어(Python 등) 에서도 지원
A 시스템(python) <-> JSON 텍스트 데이터 <-> B 시스템(타 프로그래밍 언어)"""