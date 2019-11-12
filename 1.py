from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox(executable_path="/root/Downloads/driver/geckodriver")
driver.set_page_load_timeout(10)
driver.get("https://www.youtube.com")
driver.find_element_by_name("search_query").send_keys("hello world")
driver.find_element_by_id("search-icon-legacy").send_keys(Keys.ENTER)
#driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").send_keys(Keys.ENTER)
time.sleep(4)
driver.close()


