#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 显示等待，很多网页采用Ajax技术，不确定网页元素的加载情况，选取会很困难
# 因此需要等待加载完毕，此例子是基于selenium进行的显示等待

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")

try:
    element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "myDynamicElement"))
            )
finally:
    driver.quit()

# 解析：加载页面，定位id为myDynamicElement的元素，设置超时时间为10s
# WebDriverWait默认每500ms检测元素是否存在
# Selenium提供了显示等待的方法 在expected_conditions类中


# 隐式等待，尝试查找某个元素时候，没有发现，就等待固定长度时间，类似于socket超时，默认0s
url = "http://somedomain/url_that_delays_loading"
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)
myDynamicElement = driver.find_element_by_id("myDynamicElement")

# 线程休眠方法也常用于爬取延时加载的页面
time.sleep(time)
