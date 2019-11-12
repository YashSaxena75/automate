from selenium import webdriver
import time
import optparse
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800,600))
display.start()
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox(executable_path="/root/Downloads/driver/geckodriver")
driver.set_page_load_timeout(10)
uname="admin"
passw="password"
c=0
print( '''\033[1;93m
        ___
       __H__
 ___ ___|\033[41m.\033[0m\033[1;93m|_____ ___|\  |  \033[1;97m{\033[90m1.O#stable\033[1;97m}\033[1;93m
|_ -| . |\033[41m.\033[0m\033[1;93m|     | .'| \ |
|___|_  |\033[41m.\033[0m\033[1;93m|_|_|_|__,|  \|
      |_|V                    \033[0m\033[4;37mYashSaxena\033[0m
''')
def parser():
	parser=optparse.OptionParser()
	parser.add_option("-u", "--user", dest="id", help="please specify user id")
	parser.add_option("-s", "--security",dest="sec",help="please sepcify the security")
	parser.add_option("-o", "--output",dest="op",help="Please specify the path to save the file")
	(options,arguments)=parser.parse_args()
	if not options.id:
		parser.error("[-] Please Specify the user option, Use --help for more info.")
	if not options.sec:
		parser.error("[-] Please Specify the security level, Use --help for more info.")
	return options

options=parser()
try:
	driver.get("http://127.0.0.1/DVWA/login.php")
	driver.find_element_by_name("username").send_keys(uname)
	driver.find_element_by_name("password").send_keys(passw)
	driver.find_element_by_xpath("/html/body/div/div[2]/form/fieldset/p/input").click()
	c=1
except Exception as e:

	print(e)

if c==1:
	driver.get("http://127.0.0.1/DVWA/security.php")
	f=driver.find_element_by_xpath("/html/body/div/div[3]/div/form/select")
	f.send_keys(options.sec)
	if options.sec=='Low':
		driver.find_element_by_xpath("/html/body/div/div[3]/div/form/input[1]").click()
		driver.get("http://127.0.0.1/DVWA/vulnerabilities/sqli/")
		driver.find_element_by_name("id").send_keys(options.id)
		driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/p/input[2]").click()
		str = driver.find_element_by_xpath("/html/body/div/div[3]/div/div")
		f=open(options.op,'w+')
		f.write('SQLMAN Report from DVWA (by yash saxena)')
		f.write("\n----------------------------------------------------------------------\n")
		f.write(str.text)
		f.close()
	else:
		print("This works only for low level security.")
		print("Please use burpsuite for medium level")
		print("Work in progress for high level security.")
else:
	print("0x\414141")
