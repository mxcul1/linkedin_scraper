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

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("chromedriver.exe", options=options)

driver.get("https://dev.www.tycois.com/");
industries = driver.findElement(By.cssSelector("div.columns.three.alpha > ul"))
links = industries.findElements(By.tagName("li"))
# for (int i = 0; i < links.size(); i++)
# {
#     System.out.println(links.get(i).getText());
# }