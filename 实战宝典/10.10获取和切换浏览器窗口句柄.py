# import time
# from selenium import webdriver

#
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# now_hanle=driver.current_window_handle
# print(now_hanle)
# driver.find_element_by_id('kw').send_keys('w3cshool')
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
# time.sleep(5)
# all_hanles=driver.current_window_handle
# print("++++",driver.window_handles[-1])
# # for handle in all_hanles:
# #     if handle !=now_hanle:
# #          driver.switch_to.window(handle[0])
# #driver.switch_to.window(all_hanles[1])
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="navsecond"]/ul[1]/li[2]/a').click()
# time.sleep(3)
# driver.quit()
# print(now_hanle)
# driver.switch_to.window(now_hanle[0])
# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id('kw').send_keys(u"光荣之路")
# driver.find_element_by_id('su').clear()
# time.sleep(3)
# driver.quit()











#conding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

search_windows=driver.current_window_handle

driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_link_text(u'立即注册').click()

all_handles=driver.window_handles

#进入注册窗口
for handle in all_handles:
    if handle !=search_windows:
       driver.switch_to.window(handle)
       print ('now registerwindow!')
       driver.find_element_by_name("userName").send_keys('username')
       driver.find_element_by_name('phone').send_keys('password')
       time.sleep(2)
#进入搜索窗口
for handle in all_handles:
    if handle ==search_windows:
       driver.switch_to.window(search_windows)
       print ('now sreachwindow!')
       driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
       driver.find_element_by_id("kw").send_keys("selenium")
       driver.find_element_by_id("su").click()
       time.sleep(2)

driver.quit()
