

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#查找百度首页上的“新闻”链接元素
newsElement=driver.find_element_by_xpath('//a[text()="新闻"]')
#获取查找到的“新闻”链接上的基本信息
print("元素的标签名：",newsElement.tag_name)
print("元素的ize：",newsElement.size)