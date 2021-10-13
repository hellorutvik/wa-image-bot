from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from functions import *

opt = Options()
opt.add_argument('--user-data-dir=C:\\Users\\gohil\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 13')

driver = webdriver.Chrome(options=opt)
driver.get('https://web.whatsapp.com/')

if wait_for_element(By.XPATH,'//*[@role="textbox"]',5,driver):
    print('Login Success')

# driver.find_element_by_xpath('//*[@role="textbox"]').send_keys('7405941043')

# time.sleep(3)
driver.find_element_by_xpath('//*[@data-testid="pinned"]').click()

# setup done

target_number = '7405941043'
url = f'https://api.whatsapp.com/send?phone=+91{target_number}'

ele = driver.find_element_by_tag_name('footer')

ele.find_element_by_class_name('copyable-text').send_keys(url)
ele.find_element_by_class_name('copyable-text').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@title="{}"]'.format(url)).click()

time.sleep(5)

path = 'C:\\Users\\gohil\\PycharmProjects\\Gracie\\result.jpg'

