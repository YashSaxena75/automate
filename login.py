from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox(executable_path="/root/Downloads/driver/geckodriver")
driver.set_page_load_timeout(10)
uname="test100"
passw="2525"
try:
	driver.get("http://172.16.30.200:8090/httpclient.html")
	driver.find_element_by_id("username").send_keys(uname)
	driver.find_element_by_id("password").send_keys(passw)
	driver.find_element_by_xpath("//*[@id='loginbutton']").click()
	driver.close()
	print("Login successfull with username : " + uname + "and pssword " + passw)
except Exception as e:
	print(e)

