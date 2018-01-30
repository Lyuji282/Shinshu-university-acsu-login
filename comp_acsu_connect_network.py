from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import traceback
import json
import sys 

def set_base_directory():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

def set_login_information():
    global LOGIN_ID,PASSWORD,setting_json
    setting_json = open('input.json','r')
    setting_json = json.load(setting_json)
    LOGIN_ID = setting_json['setting']['student_id']
    PASSWORD = setting_json['setting']['password']

def driver_setting():
    global driver,timeout_time
    timeout_time = 10
    options = Options()
    options.binary_location = setting_json['setting']['browser_path']
    if setting_json['setting']['headless'] == 1:
        options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options, executable_path=setting_json['setting']['chromedriver_path'])

def url_initialize():
    global url,login_name_xpath,login_pass_xpath,submit_xpath,mypage,network_xpath
    url = 'https://acsu.shinshu-u.ac.jp/ActiveCampus/module/Login.php'
    login_name_xpath = '/html/body/div[2]/div[1]/div/form/label[1]/input'
    login_pass_xpath = '/html/body/div[2]/div[1]/div/form/label[2]/input'
    submit_xpath = '/html/body/div[2]/div[1]/div/form/input[3]'
    mypage = 'https://acsu.shinshu-u.ac.jp/ActiveCampus/module/MyPage.php'
    network_xpath ='//*[@id="pac1dc0e0c33ac36a148c6574ef809b09d5_m3017_l"]/table/tbody/tr/td/a'

def display_message(message):
    title = "acsu login"
    cmd = "osascript -e 'display notification \"%s\" with title \"%s\"'" % (message, title)
    os.system(cmd)

def browsing_automation():
    try:
        driver.get(url)
        login_name_button = WebDriverWait(driver, timeout_time).until(EC.element_to_be_clickable((By.XPATH, login_name_xpath)))
        login_name_button.send_keys(LOGIN_ID)
        login_pass_button = WebDriverWait(driver, timeout_time).until(EC.element_to_be_clickable((By.XPATH, login_pass_xpath)))
        login_pass_button.send_keys(PASSWORD)
        submit_button = WebDriverWait(driver, timeout_time).until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
        submit_button.click()
        driver.get(mypage)
        network_button = WebDriverWait(driver, timeout_time).until(EC.element_to_be_clickable((By.XPATH, network_xpath)))
        network_button.click()
        time.sleep(2)
        display_message("You can use the acsu wifi now!")
        driver.quit()
    except:
        logger.debug(traceback.format_exc())
        driver.quit()
        display_message("You need to wait a moment to find the acsu wifi!")
        
def main():
    try:
        set_base_directory()
        set_login_information()
        driver_setting()
        url_initialize()
        browsing_automation()
    except:
        logger.debug(traceback.format_exc())
        display_message("Unexpected error happened.")
    
if __name__ == '__main__':
    main()
