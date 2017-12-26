

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com/")
time.sleep(3)
aElement=driver.find_element_by_xpath("//*[@class='mnav'][1]")
a_text=aElement.text
    #self.assertEqual(a_text,"米")

print(a_text)