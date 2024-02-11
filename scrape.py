import requests
from urllib.request import urlopen
from urllib.parse import quote, urlencode
import html5lib
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

# r = requests.get('https://www.linkedin.com/jobs/search/?f_JT=C%2CF&geoId=90009521&keywords=full%20stack%20engineer&location=Greater%20Melbourne%20Area')
# soup = BeautifulSoup(r.text)
# print(soup.encode("utf-8"))

# with urlopen() as f:
#     document = html5lib.parse(f, transport_encoding=f.info().get_content())

'''
input('name')
'''

def get_url():
    job_title = quote("full stack engineer")
    location = quote("Greater Melbourne Area")
    url = f"https://www.linkedin.com/jobs/search/?f_JT=C%2CF&geoId=90009521&keywords={job_title}&location={location}"

    return url

def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib').encode("utf-8")
    return soup

def selenium_tests(url):
    job_id= []
    job_title = []
    company_name = []
    location = []
    date = []
    job_link = []

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    wd = webdriver.Chrome(executable_path=r"./chromedriver.exe")
    wd.get(url)
    # no_of_jobs = int(wd.find_element_by_css_selector('h1>span').get_attribute('innerText'))
    test = wd.find_element_by_css_selector('')
    # print(no_of_jobs)
    '''
    job_lists = wd.find_element_by_class_name('jobs-search__results-list')
    jobs = job_lists.find_elements_by_tag_name('li')


    for job in jobs:
        job_id0 = job.get_attribute('data-id')
        job_id.append(job_id0)
        
        job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
        job_title.append(job_title0)
        
        company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
        company_name.append(company_name0)
        
        location0 = job.find_element_by_css_selector('[class=”job-result-card__location”]').get_attribute('innerText')
        location.append(location0)
        
        date0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
        date.append(date0)
        
        job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
        job_link.append(job_link0)

    jd = []
    seniority = []
    emp_type = []
    job_func = []
    industries = []
    for item in range(len(jobs)):
        job_func0=[]
        industries0=[]
        # clicking job to view job details
        job_click_path = f'/html/body/main/div/section[2]/ul/li[{item+1}]/img'
        job_click = job.find_element_by_xpath(job_click_path).click()
        time.sleep(5)
        
        jd_path = '/html/body/main/section/div[2]/section[2]/div'
        jd0 = job.find_element_by_xpath(jd_path).get_attribute('innerText')
        jd.append(jd0)
        
        seniority_path = '/html/body/main/section/div[2]/section[2]/ul/li[1]/span'
        seniority0 = job.find_element_by_xpath(seniority_path).get_attribute('innerText')
        seniority.append(seniority0)
        
        emp_type_path = '/html/body/main/section/div[2]/section[2]/ul/li[2]/span'
        emp_type0 = job.find_element_by_xpath(emp_type_path).get_attribute('innerText')
        emp_type.append(emp_type0)
        
        job_func_path = '/html/body/main/section/div[2]/section[2]/ul/li[3]/span'
        job_func_elements = job.find_elements_by_xpath(job_func_path)
        for element in job_func_elements:
            job_func0.append(element.get_attribute('innerText'))
            job_func_final = ', '.join(job_func0)
            job_func.append(job_func_final)
            industries_path = '/html/body/main/section/div[2]/section[2]/ul/li[4]/span'
            industries_elements = job.find_elements_by_xpath(industries_path)
        for element in industries_elements:
            industries0.append(element.get_attribute('innerText'))
            industries_final = ', '.join(industries0)
            industries.append(industries_final)
        job_data = pd.DataFrame({'ID': job_id,
            'Date': date,
            'Company': company_name,
            'Title': job_title,
            'Location': location,
            'Description': jd,
            'Level': seniority,
            'Type': emp_type,
            'Function': job_func,
            'Industry': industries,
            'Link': job_link
            })
        job_data['Description'] = job_data['Description'].str.replace('\n',' ')
        job_data.to_excel('LinkedIn Job Data_Data Scientist.xlsx', index = False)
        '''

    # return jobs
    # driver.quit()
    # return no_of_jobs
    
if __name__ == '__main__':
    url = get_url()
    #    print(get_data(url))
    jobs = selenium_tests(url)
