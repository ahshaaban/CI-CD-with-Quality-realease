# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Start the browser and login with standard_user
def login (driver, user="standard_user", password="secret_sauce"):
    #Login
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    assert 'https://www.saucedemo.com/inventory.html' in driver.current_url
    print(timestamp() +' Login successful with username '+ user + ' and password '+ password)


if __name__ == "__main__":
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()

    print (timestamp()+' Browser started successfully. Navigating to the demo page to login.')

    login(driver, 'standard_user', 'secret_sauce')
    add_cart(driver, 6)
    remove_cart(driver, 6)

    print(timestamp() + ' Selenium Tests DONE')