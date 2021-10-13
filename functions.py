import selenium, math, sys, time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchWindowException, \
    ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# import requests
# from bs4 import BeautifulSoup


def wait_for_element(method, element, time, browser, msg=None):
    try:
        WebDriverWait(browser, time).until(
            EC.presence_of_all_elements_located((method, element)))
        return True
    except TimeoutException:
        if msg:
            print('Time out {}'.format(msg))
        return False


def wait_for_element_input(method, element, keys, time, browser, msg=''):
    try:
        WebDriverWait(browser, time).until(
            EC.visibility_of_element_located((method, element))).send_keys(keys)
        return element
    except TimeoutException:
        if msg:
            print('Time out {}'.format(msg))
        return True


def wait_for_element_click(method, element, time, browser, msg=None):
    try:
        WebDriverWait(browser, time).until(EC.element_to_be_clickable((method, element))).click()
        return True
    except TimeoutException:
        if msg:
            print('Time out {}'.format(msg))
        return False


def approve_from_url(token, browser):
    browser.get(token)
    wait_for_element_click(By.NAME, 'customerResponseApproveButton', 5, browser)
