from selenium import webdriver
import time

def launch_webpage():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

def add_products_to_cart():
    #container=driver.find_element_by_class_name('container')
    container=driver.find_element_by_xpath("//div[@class='container']")
    no_of_buttons=container.find_elements_by_xpath("//div/div/descendant::button")
    print(len(no_of_buttons))
    
    for i in range(0,len(no_of_buttons)):
        add_button=driver.find_element_by_xpath("//button[text()='Add']")
        add_button.click()

def close_webpage():
    driver.quit()

if __name__ == "__main__":
    launch_webpage()
    time.sleep(2)
    add_products_to_cart()
    time.sleep(3)
    close_webpage()