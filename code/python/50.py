# selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# # driver = webdriver.Chrome()
# # driver.get("https://naver.com")
# # input("대기")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.get("https://naver.com")

# input("")

# 여기까지 webdriver 설정
# ---------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # By사용
from selenium.webdriver.common.keys import Keys  # Key사용
import time

service = Service()
driver = webdriver.Chrome(service=service)


# 브라우저 제어
# driver.get("https://google.com")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()
# time.sleep(2)
# driver.get("https://www.wikipedia.org")
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
# driver.quit()
# input("")

#########################
# 웹 상호작용
# driver.get("https://google.com")
# time.sleep(2)
# search_input = driver.find_element(By.NAME, "q")
# time.sleep(2)
# search_input.send_keys("selenium1")
# time.sleep(2)
# search_input.send_keys(Keys.BACKSPACE)
# # search_input.send_keys(Keys.ENTER)
# input("")

#####################################
# 스크롤과 창옵션
# driver.get("https://naver.com")
# time.sleep(2)
# driver.execute_script("alert('hello, selenium')")
# time.sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# time.sleep(2)
# alert.accept()  # 확인버튼 클릭

# # element창찾기
# search_input = driver.find_element(By.XPATH, '//*[@id="query"]')
# search_input.send_keys("selenium")
# search_input.send_keys(Keys.ENTER)
# input("")

##############################################
# # 무한스크롤
driver.get("https://www.google.com/imghp?hl=ko&ogbl")
search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_input.send_keys("토끼")
search_input.send_keys(Keys.ENTER)

for i in range(3):
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(2)


input("")



# 대기
driver.get("https://google.com")
driver.implicitly_wait(10)

'''
EC메서드 (대기조건)
EC.title_is(문자열) : 현재페이지 제목이 지정된 문자열과 일치할 때
EC.title_contains(문자열) : 현재페이지 제목에 문자열이 포함될 때
EC.presence_of_element_located((By.ID, "아이디값"))  #DOM이 존재할 때(화면에 표시 안 되도 됨)
EC.visibility_of_element_located((By.CSS_SELECTOR, "선택자")) #DOM이 존재할 때(화면에 표시)
EC.presence_of_all_elements_located((By.CSS_SELECTOR, "선택자")) #DOM에 모든 요소가 존재할 때
EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "선택자"))  #DOM에 모든 요소가 존재할 때
EC.element_to_be_clickable((BY.CSS_SELECTOR, "선택자"))  #요소가 화면에 표시되고 클릭이 가능할 때
EC.element_to_be_selected((BY>CSS_SELECTOR, "선택자")) # 요소가 선택된 상태가 될 때
'''

# 검색입력 필드 대기
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
search_input.send_keys("python")
search_input.send_keys(Keys.ENTER)

input("")

