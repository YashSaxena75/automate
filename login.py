from selenium import webdriver
import time
import optparse
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox(executable_path="/root/Downloads/driver/geckodriver")
driver.set_page_load_timeout(10)
def parser():
	parser=optparse.OptionParser()
	parser.add_option("-u", "--user", dest="un", help="please specify user id")
	parser.add_option("-p", "--security",dest="pa",help="please sepcify the password")
	(options,arguments)=parser.parse_args()
	if not options.un:
		parser.error("[-] Please Specify the userid , Use --help for more info.")
	if not options.pa:
		parser.error("[-] Please Specify the password, Use --help for more info.")
	return options

options=parser()

try:
	driver.get("http://172.16.30.200:8090/httpclient.html")
	driver.find_element_by_id("username").send_keys(options.un)
	driver.find_element_by_id("password").send_keys(options.pa)
	driver.find_element_by_xpath("//*[@id='loginbutton']").click()
	print("Login successfull with username : " + options.un + " and password " + options.pa)

except Exception as e:
	print(e)

