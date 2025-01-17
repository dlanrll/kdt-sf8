from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def github_login_and_crawl(username, password, user_id):
    # WebDriver 초기화 (Chrome)
    driver = webdriver.Chrome()  # 크롬 드라이버 경로를 지정해 주세요.
    driver.get("https://github.com/login")
    
    try:
        # 로그인 페이지에서 사용자 이름 및 비밀번호 입력
        login_field = driver.find_element(By.ID, "login_field")
        password_field = driver.find_element(By.ID, "password")
        login_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)  # Enter 키로 로그인

        time.sleep(3)  # 로그인 처리 대기

        # 로그인 성공 여부 확인
        if "Sign out" in driver.page_source:
            print("로그인 성공!")
        else:
            print("로그인 실패")
            return

        # 사용자 프로필 페이지로 이동
        profile_url = f"https://github.com/{user_id}"
        driver.get(profile_url)

        # 사용자 이름 크롤링
        time.sleep(2)  # 페이지 로드 대기
        name_element = driver.find_element(By.CSS_SELECTOR, "span.p-nickname")
        print("사용자 이름 :", name_element.text.strip())

    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        # 브라우저 닫기
        driver.quit()

# 실행
github_login_and_crawl("your_username", "your_password", "choi-yeong")


