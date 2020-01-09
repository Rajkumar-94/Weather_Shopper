"""
The script is an example of weather shopper
This Selenium Python code will select the least priced Moisturizer "Aloe" and "Almond" products  and adds it to the cart and takes the screenshot of the added Products

"""

from selenium import webdriver
import time

def launch_webpage():
    "This function launches the website and navigates the provided URL"
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
    
def add_aloe_product_with_least_price_to_cart(driver):
    "This function extracts only the Aloe products and adds the least costed Aloe product to the cart"
    price_mois=[]
    aloe_products=driver.find_elements_by_xpath("//p[contains(text(),'Aloe')]/following-sibling::p")
    for each_element in aloe_products:  
        price_moisturizer=int(each_element.text.split()[-1])
        price_mois.append(price_moisturizer)
    print("The list of of Moisturizer price which has Aloe in it are: ",price_mois)
    min_value=10000
    for item in price_mois:
        if item<min_value:
            min_value=int(item)
    print("The least priced Aloe product value is: ",min_value)
    Aloe_product_with_min_price=driver.find_element_by_xpath("//p[contains(text(),'%d')]/parent::div/p[contains(text(),'Aloe')]"%min_value)
    print("The least costed Aloe Product is: ",Aloe_product_with_min_price.text)
    driver.find_element_by_xpath("//p[contains(text(),'Aloe')]/following-sibling::p[contains(text(),'%d')]/following-sibling::button"%min_value).click()
    

def add_almond_product_with_least_price_to_cart(driver):
    "This function extracts only the Amond products and adds the least costed Aloe product to the cart"
    price_mois=[]
    almond_products=driver.find_elements_by_xpath("//p[contains(text(),'almond') or contains(text(),'Almond')]/following-sibling::p")
    for each_element in almond_products:  
        price_moisturizer=int(each_element.text.split()[-1])
        price_mois.append(price_moisturizer)
    print("The list of of Moisturizer price which has Almond in it are: ",price_mois)
    min_value=10000
    for item in price_mois:
        if item<min_value:
            min_value=int(item)
    print("The least priced Almond product value is: ",min_value)
    Almond_product_with_min_price=driver.find_element_by_xpath("//p[contains(text(),'%d')]/parent::div/p[contains(text(),'lmond')]"%min_value)
    print("The least costed Almond Product is: ",Almond_product_with_min_price.text)
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value).click()

def close_webpage():
    "This function closes the browser"
    driver.quit()

# Program starts here
if __name__ == "__main__":
    #This calling function will launch the webpage and navigates to the provided url.
    launch_webpage()
    time.sleep(2)
    #This calling function will add the least priced Aloe product to the cart.
    add_aloe_product_with_least_price_to_cart(driver)

    #This calling function will add the least priced Almond product to the cart.
    add_almond_product_with_least_price_to_cart(driver)

    #This Step will click and the cart button and take a Screenshot of the cart items
    cart=driver.find_element_by_xpath("//span[@id='cart']").click()
    driver.save_screenshot("screenshot.png")

    #This calling function will close the browser.
    close_webpage()



    
