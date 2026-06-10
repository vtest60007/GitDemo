from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Find search box and type
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello Selenium!")
search_box.submit()

# Close browser
# driver.quit()
