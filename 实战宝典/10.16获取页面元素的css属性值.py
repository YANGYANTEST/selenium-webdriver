import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#找到搜索输入框元素
serchBox=driver.find_element_by_id('kw')
#使用页面元素对象的value_of_css_property方法获取元素的css属性值
print("搜索输入框的高度是：",serchBox.value_of_css_property("height"))
print("搜索输入框的宽度是：",serchBox.value_of_css_property("width"))

font=serchBox.value_of_css_property("font-family")
print("搜索输入框的字体是",font)
time.sleep(2)
driver.quit()