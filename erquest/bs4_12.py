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
url="http://ordertickets.ubus.com.tw/"#讀取網頁
browser.get(url)
ele = browser.find_element_by_tag_name("frame")
time.sleep(3)
ele.send_keys(Keys.END)#Keys.END到最下面
time.sleep(3)
browser.switch_to.frame(0)
browser.find_element_by_id("i_agree").click()#click()
browser.find_element_by_id('iagree_form').click()