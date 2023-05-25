from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)
article_numbers = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_numbers.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

