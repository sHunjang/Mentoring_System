from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import openpyxl

# 크롬 드라이버 자동 업데이트를 위함
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저가 자동으로 꺼질 경우 방지 코드
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 최신 버전을 설치 후 서비스 객체를 만듦
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 웹 페이지 주소로 이동
driver.get("https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=job.popularity_order&years=0&locations=all")

# 정렬 기준을 '인기순'으로 지정하기 위한 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div/div[1]/div/div/div/div[3]/div/div[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/div/div[1]/div/div/div/div[3]/div/div[1]/ul/li[3]/button').click()

# 스크롤 횟수 지정
max_scroll_count = 3
scroll_count = 0

# 스크롤 전 높이
before_sc = driver.execute_script("return window.scrollY")

# 스크롤 진행 코드
while scroll_count < max_scroll_count :
    # 스크롤을 맨 아래로 내림
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(2) # 스크롤 사이 페이지 로딩 시간
    
    # 스크롤 후 높이
    after_sc = driver.execute_script("return window.scrollY")
    
    # 스크롤 전, 후 높이 변화가 없으면 스크롤 중지
    if after_sc == before_sc :
        break
    else :
        before_sc = after_sc
        scroll_count += 1
        

# 정보들을 담고 있는 부모 <div> 태그를 선택
items = driver.find_elements(By.CSS_SELECTOR, ".Card_className__u5rsb")

# 엑셀 파일 생성 및 시트 추가
workbook = openpyxl.Workbook()
sheet = workbook.active

# 헤더 추가
sheet.append(["Company Name", "Job Position"])


# 부모 <div> 태그 아래의 정보들을 하나씩 가져와서 엑셀에 추가
for item in items:
    company_name = item.find_element(By.CSS_SELECTOR, ".job-card-company-name").text
    job_position = item.find_element(By.CSS_SELECTOR, ".job-card-position").text
    print(company_name, job_position)
    sheet.append([company_name, job_position])

# 엑셀 파일 저장
workbook.save("Crawling_Posting.xlsx")



# driver 종료
driver.quit()


