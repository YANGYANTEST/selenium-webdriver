

import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.sougou.com")
time.sleep(3)
#获取当前的url
sougouurl=driver.current_url
print(sougouurl)
try:
    assert u"https://www.sougou.com" in sougouurl
    print('sueccss')
except Exception as e:
    print("error")

time.sleep(2)
driver.quit()