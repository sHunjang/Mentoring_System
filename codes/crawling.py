import time
import requests as rq
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import csv

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1")

#직무 탭 클릭
driver.find_element(By.PARTIAL_LINK_TEXT, '직무').click()
driver.implicitly_wait(3)

#직업 검색
search = driver.find_element(By.ID, 'lb_job_sch')
search.click()
time.sleep(3)

search.send_keys('개발자')
search.send_keys(Keys.ENTER)
time.sleep(3)

checkboxes = driver.find_elements(By.XPATH, '//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[1]/dd[2]/div[1]/div/div/dl/dd/div[1]/ul/li')
items_to_select = ['백엔드개발자', '웹개발자', '앱개발자']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..')
    label = parent.find_element(By.TAG_NAME, 'label')
    if label.text in items_to_select:
        checkbox.click()

time.sleep(3)

choice_btn = driver.find_element(By.CSS_SELECTOR, '.btn_okay.dev-searched-terms-ok')
choice_btn.click()
time.sleep(3)

search_btn = driver.find_element(By.XPATH, '//*[@id="dev-btn-search"]')
search_btn.click()
time.sleep(3)

before_sc = driver.execute_script("return window.scrollY")

while True :
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(0.5)
    
    after_sc = driver.execute_script("return window.scrollY")
    
    if after_sc == before_sc:
        break
    else :
        before_sc = after_sc

time.sleep(3)

companies = driver.find_elements(By.XPATH, '//*[@id="dev-gi-list"]/div/div[5]')

for company in companies:
    name = company.find_element(By.CSS_SELECTOR, '.tplCo').text
    field = company.find_element(By.CSS_SELECTOR, '.tplTit').text
    print([name, field])

data = []
for company in companies:
    name = company.find_element(By.CSS_SELECTOR, '.tplCo').text
    field = company.find_element(By.CSS_SELECTOR, '.tplTit').text
    data.append([name, field])

# CSV 파일로 저장
file_path = 'companies_posting.csv'
with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company', 'Field'])
    writer.writerows(data)