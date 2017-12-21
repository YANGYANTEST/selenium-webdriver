

#改变浏览器窗口的位置
#driver.get_window_position()/不支持谷歌浏览器

import time
from selenium import webdriver
driver=webdriver.Firefox()
url="http://www.baidu.com"
driver.get(url)
time.sleep(5)
#获取当前浏览器在屏幕上的位置，返回的是字典对象
position=driver.get_window_position()
print("当前浏览器所在位置的横坐标：",position['x'])
print("当前浏览器所在位置的纵坐标：",position['y'])
#设置当前浏览器在屏幕上的位置
print(driver.set_window_rect(y=200,x=400))
#设置浏览器位置后，再次获取浏览器的 位置信息
driver.get_window_position()
driver.maximize_window()
driver.close()

