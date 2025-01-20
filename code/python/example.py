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
