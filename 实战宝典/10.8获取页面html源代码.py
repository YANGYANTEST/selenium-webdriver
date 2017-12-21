

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#调用driver的page_source属性获取页面源码
pageSoure=driver.page_source
#打印源码
print(pageSoure)
#判断页面源码是否包含”百度“两个关键字，
try:
    assert u"百度一下" in pageSoure
    print("success")
except Exception as e:
    print("error")

time.sleep(2)
driver.quit()



