"""
The script is an example of weather shopper
This Selenium Python code will click on sunscreen or moisturizer based on the temperature and veriffies whether it has navigated to the expected page, adds the least priced products to the cart based on the condition, and checks the cart total and number of items. 
Completes the payment, takes the card details from the conf file and completes the transaction and checks whether the payment is successful or not.
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import test_to_add_required_moisturizer_to_cart
import test_to_add_required_Sunscreen_to_cart
import time
import conf

def launch_webpage():
    "This function launches the website and navigates the provided URL"
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
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
        test_to_add_required_moisturizer_to_cart.add_almond_product_with_least_price_to_cart(driver)
        test_to_add_required_moisturizer_to_cart.add_aloe_product_with_least_price_to_cart(driver)

    elif temp>34:
        driver.find_element_by_xpath("//button[contains(text(),'sunscreens')]").click()
        time.sleep(2)
        if(driver.title=="The Best Sunscreens in the World!"):
            print("Successly navigated to Sunscreens page based on the climate")
        else:
            print("Fail:Did not navigated to Sunscreens page")

        #This is the calling functions, which calls functions from the imported file to add least sunscreens product to the cart.
        test_to_add_required_Sunscreen_to_cart.add_SPF_50_product_with_least_price_to_cart(driver)
        test_to_add_required_Sunscreen_to_cart.add_SPF_30_product_with_least_price_to_cart(driver)

def click_cart():
    "This function navigates to the cart page, checks the cart total and number of items and takes a screenshot of the cart screen"
    driver.find_element_by_xpath("//span[@id='cart']").click()
    driver.save_screenshot("cart.png")      
    count=driver.find_elements_by_xpath("//table[contains(text(),table)]/tbody/descendant::tr")
    print("The number of products in cart are: ",len(count))
    total_price=driver.find_element_by_xpath("//p[@id='total']").text
    price=total_price.split(' ')
    print("The total cart price is: ",price[-1])

def payment():
    "This function clicks on Pay with card and takes the input details from conf file and completes the Payment, checks whether the Payment is completed successfully or not"
    pay_button=driver.find_element_by_xpath("//span[contains(text(),'Pay')]")
    pay_button.click()
    
    frame1=driver.find_element_by_xpath("//iframe[@name='stripe_checkout_app']")
    driver.switch_to_frame(frame1)
    email=driver.find_element_by_xpath("//input[@type='email']")
    email.send_keys(conf.email)
    time.sleep(5)

    #If already existing mail id is entered, the iframe navigates to next screen which sends the OTP to the registeres mail id. This try block will makes the iframe to navigate back to the card details screen to enter the card details and complete the transaction.
    try:
        existing_mail=driver.find_element_by_xpath("//span[contains(text(),'Fill in your card')]")
        existing_mail.click()
    except NoSuchElementException:
        pass
    
    time.sleep(3)
    card=driver.find_element_by_xpath("//label[contains(text(),'Card')]/following-sibling::input")
    card.send_keys(conf.card_no)
    
    
    expiry=driver.find_element_by_xpath("//label[contains(text(),'Expiry')]/following-sibling::input")
    expiry.send_keys(conf.expiry)
    
    
    cvc=driver.find_element_by_xpath("//label[contains(text(),'CVC')]/following-sibling::input")
    cvc.send_keys(conf.cvc)
    
   
    zip=driver.find_element_by_xpath("//label[contains(text(),'ZIP')]/following-sibling::input")
    zip.send_keys(conf.zip)
    
    
    checkbox=driver.find_element_by_xpath("//label[contains(text(),'Remember')]")
    checkbox.click()
    

    phone=driver.find_element_by_xpath("//label[contains(text(),'Phone')]/following-sibling::input")
    phone.send_keys(conf.phone_num)
    
    time.sleep(2)
    final_pay=driver.find_element_by_xpath("//button[@type='submit']")
    final_pay.click()
    
    driver.switch_to.default_content()
    
    time.sleep(5)
    driver.save_screenshot("screenshot.png")
    try:
        driver.find_element_by_xpath("//h2[text(),'PAYMENT SUCCESS')]")
    except NoSuchElementException:
        #This pattern of catching all exceptions is ok when you are starting out
        result_flag = False 
    else:
        result_flag = True

    if result_flag is True:
        result=driver.find_element_by_xpath("//p[@class='text-justify']").text
        print(result)
    else:
        result=driver.find_element_by_xpath("//p[@class='text-justify']").text
        print(result)
    
    
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

    #This calling funtion will complete the payment and checks whether the payment is successful or not.
    payment()

    #This calling function will close the browser.
    close_webpage()