#coding:utf-8

# 爬取去哪儿网的酒店信息

# 第一步找到酒店信息，通过selenium获取目的地框，入住日期，离店日期。
# driver 看 waitAjax.py 这个脚本
ele_toCity = driver.find_element_by_name('toCity')
ele_fromDate = driver.find_element_by_name('fromDate')
ele_toDate = driver.find_element_by_name('toDate')
ele_search = driver.find_element_by_name('search-btn')

ele_toCity.clear() # 清除当前默认
ele_toCity.send_keys(to_city) # 发送要搜索的城市
ele_toCity.click() # 点击
ele_fromDate.clear() 
ele_fromDate.send_keys(fromDate)
ele_toDate.clear()
ele_toDate.send_keys(todate)
ele_search.click()

# 分两次获取一页完整的数据，第二次让driver执行js脚本
try:
    WebDriverWait(driver, 10).until(
                EC.title_contains((to_city))
            )
except Exception, e:
    print(e)
    break
time.sleep(5)

js = "window.scrollTo(0,document.body.scrollHeight);"
driver.execute_script(js)
time.sleep(5)
htm_const = driver.page_source

# 第三步，使用BeautifulSoup解析酒店信息，将数据进行清洗和存储

soup = BeautifulSoup(htm_const, 'html.parser', from_encoding='utf-8')
infos = soup.find_all(class_='item_hotel_info')
f = coddecs.open(unicode(to_city)+unicode(fromDate)+u'.html', 'a', 'utf-8')
for info in infos:
    f.write(str(page_num)+'---'*50)
    content = info.get_text().replace(" ", "").replace("\t", "").strip()
    for line in [ln for ln in content.splitlines() if ln.strip()]:
        f.write(line)
        f.write('\r\n')
    f.close()

# 第四步：点击下一页重复
nex_page = WebDriverWait(driver, 10).until(
            EC.visibility_of(driver.find_element_by_css_selector(".item.next"))
        )
nex_page.click()






