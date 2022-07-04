import requests 
from bs4 import BeautifulSoup 

def get_query_param():
    print("Print a job name: ")
    job_name = input()
    return job_name

job_name = get_query_param()

url_addr = 'https://irkutsk.hh.ru/search/vacancy?text={}'.format(job_name)


data = requests.get(url_addr)

soup = BeautifulSoup(data.text, 'html.parser')

print(data.content)