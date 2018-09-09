import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://m.weibo.cn/')

driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[2]/div').click()
time.sleep(3)

login = {
    # key: value
    'username': 'yoyilife@163.com',
    'password': 'yoyi2018'
}
driver.find_element_by_xpath('//p/input[@id="loginName"]').send_keys(login['username'])
driver.find_element_by_xpath('//p/input[@id="loginPassword"]').send_keys(login['password'])
driver.find_element_by_xpath('//a[@id="loginAction"]').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@class="prf-handle m-box"]/div[@class="m-box-center-a"]/span[3]').click()
time.sleep(3)

count = 0
from_dict = dict()
info_xpath = '//*[@id="app"]/div/div[2]/div[@class="card card11"]/div/div/' \
             'div[@class="card m-panel card28 m-avatar-box"]' + \
             '/div[@class="card-wrap"]/div/div/div[@class="m-box-col m-box-dir m-box-center"]/div/h4[2]'
roll_down = "var q=document.documentElement.scrollTop=100000"

elements = driver.find_elements_by_xpath(info_xpath)
num_users = len(elements)
offset = num_users - 20
num_users -= offset
print('num users: %d' % num_users)
while True:
    if count >= num_users:
        break
    from_text = driver.find_elements_by_xpath(info_xpath)[count + offset].text.lstrip('来自')
    if from_text in from_dict.keys():
        from_dict[from_text] += 1
    else:
        from_dict[from_text] = 1
    count += 1
    print('%d: %s' % (count, from_text))
    if count % 10 == 0:
        driver.execute_script(roll_down)
        time.sleep(3)
        elements = driver.find_elements_by_xpath(info_xpath)
        if num_users % 20 == 0 and num_users == len(elements):
            driver.execute_script(roll_down)
            time.sleep(30)
            elements = driver.find_elements_by_xpath(info_xpath)
        num_users = len(elements) - offset
        print('num users: %d' % num_users)

# driver.close()

print('\nNumber of users: %d' % num_users)
for f in sorted(from_dict.keys()):
    print('%s: %d' % (f, from_dict[f]))

print('\naini')