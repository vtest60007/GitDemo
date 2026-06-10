from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    # Launch Chrome browser (you can switch to Edge by using webdriver.Edge())
    driver = webdriver.Chrome()

    # Open the local HTML file (update the path if needed)
    driver.get("file:///C:/Cohorts/locators.html")

    # Print the page title
    print(driver.title)

    # Locate element by tag name <h2> and print its text
    section_name = driver.find_element(By.TAG_NAME, "h2")
    print(section_name.text)

    # Locate radio button using XPath and check its state
    gender = driver.find_element(By.XPATH, "//form/label/input[@value='m']")
    print("Is radio button selected before clicking:", gender.is_selected())
    gender.click()  # Click the radio button
    print("Is radio button selected after clicking:", gender.is_selected())
    print("Value of selected radio button:", gender.get_attribute("value"))

    # Locate first name input by ID, clear it, and enter new text
    fname = driver.find_element(By.ID, "fname")
    print(fname.get_attribute("value"))
    fname.clear()
    print(fname.get_attribute("value"))
    fname.send_keys("Venkatesh")
    print(fname.get_attribute("value"))

    # Locate last name input by ID, clear it, and enter new text
    lname = driver.find_element(By.ID, "lname")
    print(lname.get_attribute("value"))
    lname.clear()
    print(lname.get_attribute("value"))
    lname.send_keys("Iyengar")
    print(lname.get_attribute("value"))

    # Locate checkbox by NAME and check its state before and after clicking
    checkbox = driver.find_element(By.NAME, "newsletter")
    print("Is the checkbox selected before clicking:", checkbox.is_selected())
    checkbox.click()
    print("Is the checkbox selected after clicking:", checkbox.is_selected())

    # Locate link by partial link text and click it
    # Other options: By.TAG_NAME("a") or By.LINK_TEXT("Google Page")
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
    link.click()

    # Print the new page title after navigation
    print(driver.title)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
