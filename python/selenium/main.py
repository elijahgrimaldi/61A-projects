from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "/Users/eligrimaldi/Documents/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://python.org")
# search_bar = driver.find_element("name","q")
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element("class name", "python-logo")
# print(logo.size)
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(events)
driver.close()