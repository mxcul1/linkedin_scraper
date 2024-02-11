import pandas as pd
import re

from bs4 import BeautifulSoup, Tag, NavigableString
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()
from selenium.webdriver.common.keys import Keys
from warnings import warn


url = "https://www.linkedin.com/jobs/search/?f_JT=C%2CF&geoId=90009521&keywords=full%20stack%20engineer&location=Greater%20Melbourne%20Area"
no_of_jobs = 25
# this will open up new window with the url provided above 
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get(url)
sleep(3)
action = ActionChains(driver)

# to show more jobs. Depends on number of jobs selected
i = 2
while i <= (no_of_jobs/25): 
    driver.find_element_by_xpath('/html/body/main/div/section/button').click()
    i = i + 1
    sleep(5)
# parsing the visible webpage
pageSource = driver.page_source
lxml_soup = BeautifulSoup(pageSource, 'lxml')

# searching for all job containers
job_container = lxml_soup.find('ul', class_ = 'jobs-search__results-list')

print('You are scraping information about {} jobs.'.format(len(job_container)))

# setting up list for job information
job_id = []
post_title = []
company_name = []
post_date = []
job_location = []
job_desc = []
level = []
emp_type = []
functions = []
industries = []

# job_container = job_container[1::2]
# for loop for job title, company, id, location and date posted
# print(type(job_container))
# a = [x for x in job_container if (type(x) == "<class 'bs4.element.Tag'>")]
job_container = ([x for x in job_container if isinstance(x,Tag)])

# for i in a:
#     print(type(a))
for job in job_container:
    # print(job)
# driver.quit()
    # job = job[1::2]
    # print(type(job))
    # pass


    # job title
    # job_titles = job.find("span", class_="base-search-card__title").text
    job_titles = (job.find('h3'))
    
    # print(job.find_all("h3", {"class": "base-search-card__title"}).text)
    
    post_title.append(job_titles.text.strip())
    
    # job_ids = job.find('a', href=True)['href']
    # print(job_ids)
    # linkedin job id
    
    job_ids = job.find('a', href=True)['href']
    job_ids = re.findall(r'(?!-)([0-9]*)(?=\?)',job_ids)[0]
    job_id.append(job_ids)
    
    # company name
    company_names = job.select_one('img')['alt']
    company_name.append(company_names)

    # job_locations = job.find("span").text
    # print(job)
    
    # job location
    # job_locations = job.find("span", class_="job-result-card__location").text
    job_locations = job.find("span", class_="job-search-card__location").text
    
    job_location.append(job_locations)
    
    # posting date
    post_dates = job.select_one('time')['datetime']
    post_date.append(post_dates)

# for loop for job description and criterias

for x in range(1,len(job_id)+1):
    # clicking on different job containers to view information about the job
    # job_xpath = '/html/body/main/div/section/ul/li[{}]/img'.format(x)
    # print(x)
    job_xpath = f'/html/body/div[1]/div/main/section[2]/ul/li[{x}]/div/a'
    print(job_xpath)
    # driver.find_element_by_xpath(job_xpath).click()
    driver.find_element_by_xpath(job_xpath).send_keys(Keys.ENTER)
    sleep(1)
    
    # job description
    # jobdesc_xpath = '/html/body/main/section/div[2]/section[2]/div'
    jobdesc_xpath = '/html/body/div[1]/div/section/div[2]/section[2]/div/section/div'
    job_descs = driver.find_element_by_xpath(jobdesc_xpath)
    # print(type(job_descs))
    job_desc.append(job_descs.text)
    # test = driver.find_element_by_xpath("//div[@id='...']/ul/li")
    
    # html_list = self.driver.find_element_by_id("myId")
    items = job_descs.find_elements_by_tag_name("ul")
    for item in items:
        each_items = item.find_elements_by_tag_name("li")
        # print(each_items.text)
        for a in each_items:
            print(a)
        #     print(text)
    # print(items)
    # each_items = items.find_elements_by_tag_name("li")
    # for item in each_items:
    #     text = item.text
    #     print(text)
    # print(job_desc)

    # driver.findElement(By.xpath("//strong")).getText()
    '''
    # job criteria container below the description
    job_criteria_container = lxml_soup.find('ul', class_ = 'job-criteria__list')
    all_job_criterias = job_criteria_container.find_all("span", class_='job-criteria__text job-criteria__text--criteria')
    
    # Seniority level
    seniority_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[1]'
    seniority = driver.find_element_by_xpath(seniority_xpath).text.splitlines(0)[1]
    level.append(seniority)
    
    # Employment type
    type_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[2]'
    employment_type = driver.find_element_by_xpath(type_xpath).text.splitlines(0)[1]
    emp_type.append(employment_type)
    
    # Job function
    function_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[3]'
    job_function = driver.find_element_by_xpath(function_xpath).text.splitlines(0)[1]
    functions.append(job_function)
    
    # Industries
    industry_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[4]'
    industry_type = driver.find_element_by_xpath(industry_xpath).text.splitlines(0)[1]
    industries.append(industry_type)
    
    x = x+1

print(len(job_id))
print(len(post_date))
print(len(company_name))
print(len(post_title))
print(len(job_location))
print(len(job_desc))
print(len(level))
print(len(emp_type))
print(len(functions))
print(len(industries))

print(post_title)
print(company_name)
'''
driver.quit()


#   Task - Fix this
######################################################################
#   Fix the program, there will be two issues and one will not let
#   the program RUN. This is known as a Syntax Error.
#
#   Before you can RUN this code you will need to highlight the code
#   that is required to RUN, and select ALT+4 or highlight the text,
#   then select Format -> Uncomment Region. You will see the code go
#   from RED to colored.


company = ""
location = "."

# print("I work for"  company + ", it is a great company. I'm located in  + location)