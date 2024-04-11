#from coding.github.personal.data_projects.company_financials_stock_price_analysis.interfaces.ISessionHandler import ISessionHandler
from interfaces.ISessionHandler import ISessionHandler
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class YFSessionHandler(ISessionHandler):

      def __init__(self):
            self.session = self.new_session()
            time.sleep(1)
            self.crumb = self.new_crumb()

      def new_session(self):
            self.session = requests.Session()
            requests.utils.add_dict_to_cookiejar(self.session.cookies, self.__get_site_cookies())

      def new_crumb(self, retries=0, max_retries=3):
            if retries >= max_retries:
                  print("Could not retrieve crumb!")
                  return ""
            url = "https://query1.finance.yahoo.com/v1/test/getcrumb"
            self.session.headers = self.__headers()
            response = self.session.get(url)
            if response.status_code != 200:
                  print(response.text)
                  print(response.status_code)
                  print("Failed to retrieve crumb, retrying...")
                  time.sleep(1)
                  retries += 1
                  return self.new_crumb(retries=retries)
            self.crumb = response.text
            print("Successfully retrieved crumb: ", self.crumb)

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

      def __headers(self):
            headers = {
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  "Accept-Encoding": "gzip, deflate, br, zstd",
                  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                  "Cache-Control": "no-cache",
                  "Pragma": "no-cache",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            }
            return headers