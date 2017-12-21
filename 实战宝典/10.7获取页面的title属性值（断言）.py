

import time
from  selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#获取页面的title
title=driver.title
#打印出当前页面的title
print("当前页面title属性值为：",title)

#断言页面的title属性值是否是否是“百度一下，，你就知道”
try:
    assert u"百度一下" in driver.title
    print ('Assertion test pass.')
except Exception as e:
    print ('Assertion test fail.', format(e))
time.sleep(3)
driver.quit()
