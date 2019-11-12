from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox(executable_path="/root/Downloads/driver/geckodriver")
driver.set_page_load_timeout(10)
uname="test"
passw="test"
driver.get("http://testphp.vulnweb.com/login.php")
driver.find_element_by_name("uname").send_keys(uname)
driver.find_element_by_name("pass").send_keys(uname)
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/table/tbody/tr[3]/td/input").send_keys(Keys.ENTER)
#driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").send_keys(Keys.ENTER)
time.sleep(4)
driver.close()

