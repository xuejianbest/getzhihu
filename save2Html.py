from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
        
url = 'https://***'
driver = webdriver.Chrome()
driver.get(url)

def execute_times(times):
    '''每隔一定时间往下滚动一次页面，共滚动times次'''
    for i in range(times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.3)

#点开显示所有xxx个答案
try:
    driver.find_element_by_class_name("QuestionMainAction").click()
except NoSuchElementException:
    pass

#点开问题描述显示全部
try:
    driver.find_element_by_css_selector("button[class='Button QuestionRichText-more Button--plain']").click()
except NoSuchElementException:
    pass

execute_times(50)
#获得html内容
html=driver.page_source

with open("source.html", "w", encoding='utf-8') as file:
    file.write(html)
    file.close

print("将网页写入source.html完成...")