import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#获取浏览器的窗口大小，返回一个字典类型
sizedict=driver.set_window_size()
print("当前浏览器窗口的宽：",sizedict['width'])
print("当前浏览器窗口的高：",sizedict['height'])
#设置浏览器窗口的大小，set_window_size
driver.set_window_size(width=200,height=400,windowHandle='current')
#设置好，再次调用获取到窗口大小信息
print(driver.get_window_size(windowHandle='current'))
time.sleep(3)
driver.quit()

