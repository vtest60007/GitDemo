from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def main():
    # Launch Chrome browser
    driver = webdriver.Chrome()

    # Navigate to the web form page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Maximize the browser window
    driver.maximize_window()

    # Print the page title
    print(driver.title)

    # Locate text box by ID and interact with it
    text_box = driver.find_element(By.ID, "my-text-id")
    print(text_box.get_attribute("value"))  # Print initial value
    text_box.send_keys("Venkatesh")         # Enter text
    print(text_box.get_attribute("value"))  # Print updated value

    # Locate password field by NAME and interact with it
    password_field = driver.find_element(By.NAME, "my-password")
    print(password_field.get_attribute("value"))
    password_field.send_keys("Venkat")
    print(password_field.get_attribute("value"))

    # Locate textarea field by NAME and interact with it
    text_area_field = driver.find_element(By.NAME, "my-textarea")
    print(text_area_field.get_attribute("value"))
    text_area_field.send_keys("Siruseri")
    print(text_area_field.get_attribute("value"))

    # Locate disabled text box and check if it’s enabled
    disabled_text_box = driver.find_element(By.NAME, "my-disabled")
    print(disabled_text_box.get_attribute("value"))

    if disabled_text_box.is_enabled():
        disabled_text_box.send_keys("Venky")  # Will not execute since field is disabled
    print(disabled_text_box.get_attribute("value"))

    # Locate read-only text box and try to send keys
    read_only_text_box = driver.find_element(By.NAME, "my-readonly")
    print(read_only_text_box.get_attribute("value"))
    read_only_text_box.send_keys("Venky")  # Read-only fields usually ignore input
    print(read_only_text_box.get_attribute("value"))

    # Locate dropdown element
    drop_down = driver.find_element(By.NAME, "my-select")
    select = Select(drop_down)

    # Select option by index (0-based)
    select.select_by_index(3)
    time.sleep(2)

    # Select option by value attribute
    select.select_by_value("2")
    time.sleep(2)

    # Select option by visible text
    select.select_by_visible_text("Three")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
