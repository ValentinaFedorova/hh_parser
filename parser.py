from typing import final
import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent


def get_query_param():
    print("Print a job name: ")
    job_name = input()
    return job_name

skills_list = []
#job_name = get_query_param()
job_name = "backend"
url_addr = 'https://irkutsk.hh.ru/search/vacancy?text={}'.format(job_name)

useragent = UserAgent()

options = webdriver.ChromeOptions()
#options.add_argument(f"user-agent={useragent.random}")
#options.binary_location = '/Applications/Google Chrome Beta.app'

# data = requests.get(url_addr)

# soup = BeautifulSoup(data.text, 'html.parser')

driver = webdriver.Chrome(executable_path="/Users/romanfedorov/Documents/my_projects/hh_parser/chromedriver", options=options) 
subdriver = webdriver.Chrome(executable_path="/Users/romanfedorov/Documents/my_projects/hh_parser/chromedriver", options=options) 

try:
    driver.get(url_addr)
    time.sleep(5)
    #vacancy_class = driver.find_elements_by_class_name("bloko-link")
    vacancy_class = driver.find_elements(By.CLASS_NAME, "vacancy-serp-item")
    for el in vacancy_class:
        link_tag = el.find_element(By.CLASS_NAME, "bloko-link")
        link = link_tag.get_attribute("href")
        try:
            subdriver.get(link)
            time.sleep(5)
            vacancy_info = subdriver.find_elements(By.CLASS_NAME, "vacancy-description")
            for v_div in vacancy_info:
                vacancy_section = v_div.find_elements(By.CLASS_NAME,"vacancy-section")
                for vac in vacancy_section:
                    if (vac.text.lower()[0:15] == 'ключевые навыки'):
                        skills_list += vac.text.lower().split('\n')[1:]

        except Exception as ex:
            print(ex)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

res = ''
for el in skills_list:
    res += el + '\n'

f = open('skills_list.csv',"w")
f.write(res)
f.close()

print("done")