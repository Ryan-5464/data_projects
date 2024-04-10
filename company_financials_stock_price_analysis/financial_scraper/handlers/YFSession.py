from handlers.ISession import ISession
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class YFSession(ISession):

      def __init__(self):
            self.session = self.new_session()
            self.crumb = self.new_crumb()

      def new_session(self) -> requests.Session:
            session = requests.Session()
            requests.utils.add_dict_to_cookiejar(session.cookies, self.__get_site_cookies())
            return session

      def new_crumb(self, retries=0, max_retries=3) -> str:
            if retries >= max_retries:
                  print("Could not retrieve crumb!")
                  return ""
            url = "https://query1.finance.yahoo.com/v1/test/getcrumb"
            response = requests.get(url)
            if response.status_code != 200:
                  print("Failed to retrieve crumb, retrying...")
                  time.sleep(1)
                  retries += 1
                  return self.new_crumb(retries=retries)
            crumb = response.text
            print("Successfully retrieved crumb: ", crumb)
            return crumb

      def __get_site_cookies(self, retries=0, max_retries=3) -> dict:
            if retries >= max_retries:
                  print("Could not retrieve crumb!")
                  return {}
            try:
                  driver = webdriver.Chrome()
                  driver.get("https://uk.finance.yahoo.com/")
                  button = driver.find_element(by=By.CLASS_NAME, value="btn.secondary.accept-all")
                  button.click()
                  all_cookies=driver.get_cookies()
                  cookies_dict = {}
                  for cookie in all_cookies:
                        cookies_dict[cookie['name']] = cookie['value']
                  driver.quit()
            except Exception as exception:
                  print(exception, "Failed to retrieve cookies, retrying...")
                  time.sleep(1)
                  retries += 1
                  return self.new_crumb(retries=retries)
            print("Succesfully retrieved cookies: ", cookies_dict)
            return cookies_dict