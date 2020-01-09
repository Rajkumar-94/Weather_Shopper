"""
The script is an example of weather shopper
This Selenium Python code will select all the moisturizer items to the cart

"""

from selenium import webdriver
import time

def launch_webpage():
    "This function launches the website and navigates the provided URL"
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

def add_products_to_cart():
    "This function adds the available products to the cart"
    container=driver.find_element_by_xpath("//div[contains(@class,'container')]/div[descendant::div[contains(@class,'text-center')]]")
    no_of_buttons=container.find_elements_by_xpath("//button[contains(text(),'Add')]")
    #container=driver.find_element_by_class_name('container')
    #container=driver.find_element_by_xpath("//div[@class='container']")
    #no_of_buttons=container.find_elements_by_xpath("//div/div/descendant::button")
    #print(len(no_of_buttons))
    
    for i in range(0,len(no_of_buttons)):
        add_button=driver.find_element_by_xpath("//button[contains(text(),'Add')]")
        add_button.click()

def close_webpage():
    "This function closes the browser"
    driver.quit()

# Program starts here
if __name__ == "__main__":
    #This calling function will launch the webpage and navigates to the provided url.
    launch_webpage()
    time.sleep(2)

    #This calling function will add all the products in the Web page to the cart.
    add_products_to_cart()
    time.sleep(3)

    #This calling function will close the browser.
    close_webpage()