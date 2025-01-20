### KBO 성적표 크롤링하기

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 사이트 URL
url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"

# 요청 보내기
response = requests.get(url)
response.encoding = "utf-8"  # 응답 인코딩 설정

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 테이블 선택
table = soup.select_one("#cphContents_cphContents_cphContents_udpRecord > table")

# 테이블 데이터 파싱
data = []
headers = []

# 헤더 가져오기
header_row = table.find("thead").find_all("th")
headers = [header.text.strip() for header in header_row]

# 데이터 가져오기
rows = table.find("tbody").find_all("tr")
for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# 데이터프레임 생성
df = pd.DataFrame(data, columns=headers)

# txt 파일로 저장
txt_filename = "team_rankings.txt"
df.to_csv(txt_filename, sep="\t", index=False, encoding="utf-8")

print(f"크롤링한 데이터가 '{txt_filename}' 파일로 저장되었습니다.")

import pandas as pd

# 파일 읽기
file_path = "team_rankings.txt"
data = pd.read_csv(file_path, sep="\t", encoding="utf-8")

# 출력 포맷
print("=========== 2024 한국 프로야구 성적표 ===========")
print("순위\t팀\t승\t패\t무\t승률")
for i in range(len(data)):
    print(f"{data.loc[i, '순위']}\t{data.loc[i, '팀명']}\t{data.loc[i, '승']}\t{data.loc[i, '패']}\t{data.loc[i, '무']}\t{data.loc[i, '승률']}")



""" 그냥 내가 해보고 싶은 것, K리그는 POST 방식으로 크롤링하여 홈과 원정의 승률 차이를 분석하고자 함
post방식의 동적 크롤링을 하면 안되는게 아니라 그냥 selenium과 post방식 두 가지의 동적 크롤링 방법이 있는데, 기간 조회와 같은 복잡한 건 post
ui상의 정보를 뽑아내고 싶을 때는 그냥 selenium을 쓰면 되는 거 아닐까? """

import requests
import pandas as pd

# URL 및 요청 데이터 설정
url = "https://www.kleague.com/record/teamRank.do"
data = {
    'leagueId': '1',   # K리그1
    'year': '2024',    # 년도
    'stadium': 'home', # 홈 경기
    'recordType': 'rank' # 순위 데이터
}

# POST 요청 보내기
response = requests.post(url, data=data)

# 응답 상태 코드 확인
if response.status_code == 200:
    print("데이터 요청 성공!")
    
    # JSON 데이터를 파싱하여 구조 확인
    json_data = response.json()
    print(json_data)  # JSON 구조 확인

    # 데이터프레임으로 변환
    try:
        df = pd.DataFrame(json_data['data']['teamRank'])  # 정확한 키로 접근
        print(df)

        # CSV 파일로 저장 (UTF-8 BOM 포함)
        df.to_csv("k_league_home_data.csv", index=False, encoding="utf-8-sig")  # 한글 깨짐 방지
        print("데이터가 'k_league_home_data.csv' 파일에 저장되었습니다.")
    except KeyError as e:
        print(f"JSON 키 오류: {e}")
        print("JSON 데이터 구조를 확인하세요.")
else:
    print(f"데이터 요청 실패! 상태 코드: {response.status_code}")
