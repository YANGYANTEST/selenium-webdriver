import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)
# h=driver.current_window_handle
# s=driver.find_element_by_css_selector(".tab>a")
# r=[u"百度一下",u"贴吧",u"知道",u"音乐",u"图片",u"视频",u"地图",u"百科",u"文库"]
#
# for a,b in zip(s,r):
#     a.click()
#     text=a.text
#     time.sleep(2)
#     all_h=driver.window_handles
#
#     for i in all_h:
#         if i!=h:
#             driver.switch_to.window(i)
#             time.sleep(1)
#     print(driver.title)
#     if b in driver.title:
#         print(text+u"页面打开正常")
#     else:
#         print(text + u"页面测试失败")
#     driver.close()
#     driver.switch_to.window(h)
#
# driver.quit()

# driver.find_element_by_id('kw').send_keys("selenium")
# #模拟enter键操作回车按钮
# driver.find_element_by_id('su').send_keys(Keys.ENTER)
# time.sleep(5)
# driver.find_element_by_id('su').send_keys(Keys.ENTER)

driver.implicitly_wait(2)
#鼠标停留在设置按钮上
mouse=driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
driver.quit()