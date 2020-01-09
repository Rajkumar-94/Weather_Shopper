"""
The script is an example of weather shopper
This Selenium Python code will click on sunscreen or moisturizer based on the temperature and veriffies whether it has navigated to the expected page, adds the least priced products to the cart based on the condition, and checks the cart total and number of items. 

"""

from selenium import webdriver
import add_required_moisturizer_to_cart
import add_required_Sunscreen_to_cart
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
        
        driver.find_element_by_xpath("//button[contains(text(),'moisturizers')]").click()
        time.sleep(2)

        if(driver.title=="The Best Moisturizers in the World!"):
            print("Successly choosed Moistursizers based on the climate")
        else:
            print("Fail:Did not navigated to Moistursizers page")
        
        #This is the calling functions, which calls functions from the imported file to add least moisturizers product to the cart.
        add_required_moisturizer_to_cart.add_almond_product_with_least_price_to_cart(driver)
        add_required_moisturizer_to_cart.add_aloe_product_with_least_price_to_cart(driver)

    elif temp>34:
        driver.find_element_by_xpath("//button[contains(text(),'sunscreens')]").click()
        time.sleep(2)
        if(driver.title=="The Best Sunscreens in the World!"):
            print("Successly navigated to Sunscreens page based on the climate")
        else:
            print("Fail:Did not navigated to Sunscreens page")

        #This is the calling functions, which calls functions from the imported file to add least sunscreens product to the cart.
        add_required_Sunscreen_to_cart.add_SPF_50_product_with_least_price_to_cart(driver)
        add_required_Sunscreen_to_cart.add_SPF_30_product_with_least_price_to_cart(driver)

def click_cart():
    "This function navigates to the cart page, checks the cart total and number of items and takes a screenshot of the cart screen"
    driver.find_element_by_xpath("//span[@id='cart']").click()
    driver.save_screenshot("cart.png")      
    count=driver.find_elements_by_xpath("//table[contains(text(),table)]/tbody/descendant::tr")
    print("The number of products in cart are: ",len(count))
    total_price=driver.find_element_by_xpath("//p[@id='total']").text
    price=total_price.split(' ')
    print("The total cart price is: ",price[-1])

def close_webpage():
    "This function closes the browser"
    driver.quit()

# Program starts here
if __name__ == "__main__":
    #This calling function will launch the webpage and navigates to the provided url.
    launch_webpage()

    #This calling will get the displayed temperature.
    get_climate_temperature()

    #This calling function will choose sunscreen or moisturizer based on the obtained temperature.
    choose_product_based_on_climate()

    #This calling function which navigates to cart screen.
    click_cart()

    #This calling function will close the browser.
    close_webpage()
