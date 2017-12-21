#访问某个网址，进行前进/后退/刷新/窗口最大化操作

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
# assert driver.title.find(u"百度")>0,'assert error'
driver.get("http://souhu.com")
time.sleep(3)
#后退
driver.back()
time.sleep(3)
#前进
driver.forward()
#窗口最大化
driver.maximize_window()
#刷新
driver.refresh()
driver.close()

