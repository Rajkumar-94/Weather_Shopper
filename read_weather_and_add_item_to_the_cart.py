"""
The script is an example of weather shopper
This Selenium Python code will click on sunscreen or moisturizer based on the temperature and veriffies whether it has navigated to the expected page

"""

from selenium import webdriver
import time

def launch_webpage():
    "This function launches the website and navigates the provided URL"
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/")
    time.sleep(3)
    
def get_climate_temperature():  
    "This function extracts the available temperature and stores it as integer"
    temperature=driver.find_element_by_xpath("//span[@id='temperature']").text
    global temp
    temp=int(temperature.split()[0])
    print("The Temperature is: ",temp)

def choose_product_based_on_climate():
    "This function includes the condition whether to choose sunscreen or moisturizer based on the extracted temperature and checks whether it has navigated to the expected screen"
    if temp<19:
        #driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
        driver.find_element_by_xpath("//button[contains(text(),'moisturizers')]").click()
        time.sleep(2)

        if(driver.title=="The Best Moisturizers in the World!"):
            print("Successly choosed Moistursizers based on the climate")
        else:
            print("Fail:Did not navigated to Moistursizers page")

    elif temp>34:
        #driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
        driver.find_element_by_xpath("//button[contains(text(),'sunscreens')]").click()
        time.sleep(2)
        if(driver.title=="The Best Sunscreens in the World!"):
            print("Successly navigated to Sunscreens page based on the climate")
        else:
            print("Fail:Did not navigated to Sunscreens page")

def close_webpage():
    driver.quit()

# Program starts here
if __name__ == "__main__":
    #This calling function will launch the webpage and navigates to the provided url.
    launch_webpage()

    #This calling will get the displayed temperature.
    get_climate_temperature()

    #This calling function will choose sunscreen or moisturizer based on the obtained temperature.
    choose_product_based_on_climate()

    #This calling function will close the browser.
    close_webpage()
