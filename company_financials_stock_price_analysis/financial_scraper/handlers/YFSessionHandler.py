import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from handlers.ISessionHandler import ISessionHandler

class YFSessionHandler(ISessionHandler):

    def __init__(self):
        pass
    
    @classmethod
    def new_session(cls):
        session = requests.Session()
        requests.utils.add_dict_to_cookiejar(session.cookies, cls.__get_site_cookies())
        return session
        
    @staticmethod
    def __get_site_cookies():
        driver = webdriver.Chrome(executable_path=r"~/webdriver/google-chrome-stable_current_amd64.deb")
        driver.get("https://uk.finance.yahoo.com/")
        button = driver.find_element(by=By.CLASS_NAME, value="btn.secondary.accept-all")
        button.click()
        all_cookies=driver.get_cookies();
        cookies_dict = {}
        for cookie in all_cookies:
                cookies_dict[cookie['name']] = cookie['value']
        return cookies_dict