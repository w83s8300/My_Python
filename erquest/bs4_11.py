from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
options = Options()
options.add_argument("--no-sandbox") #bypass OS security model
#options.add_argument("headless")
#課本 7-32

browser=webdriver.Chrome(options=options)
browser.set_window_size(900,900)
browser.implicitly_wait(20)
url="http://ordertickets.ubus.com.tw/"
browser.get(url)

"""

ele.send_keys(Keys.END)#Keys.END到最下面
browser.find_element_by_id("bLogin").click()#click()是只點一下
browser.find_element_by_id("bLogin").click()#click()是只點一下
"""
"""
ele = browser.find_element_by_tag_name("body")
time.sleep(3)
ele.send_keys(Keys.END)#Keys.END到最下面
"""
email = "w83s8300@gmail.com"#輸入email
password = "cn231y0"#輸入密碼

"""
browser.find_element_by_name("email").send_keys(email)#send_keys是要輸入的文字
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_id("bLogin").click()#click()是只點一下
"""
