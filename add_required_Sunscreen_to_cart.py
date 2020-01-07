"""
The script is an example of weather shopper
This Selenium Python code will select the least priced Sunscreen "SPF-50" and "SPF-30" products and adds it to the cart and takes the screenshot of the added Products

"""

from selenium import webdriver

import time

def launch_webpage():
    "This function launches the website and navigates the provided URL"
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
    driver.save_screenshot('Product_list.png')

def add_SPF_50_product_with_least_price_to_cart(driver):
    "This function extracts only the SPF-50 products and adds the least priced SPF-50 product to the cart"
    spf_50_price=[]
    sunscreen_spf_50_products=driver.find_elements_by_xpath("//p[contains(text(),'SPF-50') or contains(text(),'spf-50')]/following-sibling::p")
    for each_element in sunscreen_spf_50_products:  
        price=int(each_element.text.split()[-1])
        spf_50_price.append(price)
    print("The list of of Sunscreen price which belongs to SPF-50 are: ",spf_50_price)
    min_value=10000
    for item in spf_50_price:
        if item<min_value:
            min_value=int(item)
    print("The least priced Sunscreen SPF-50 value is: ",min_value)
    sunscreen_sp5_50_product_with_min_price=driver.find_element_by_xpath("//p[contains(text(),'%d')]/parent::div/p[contains(text(),'SPF-50')]"%min_value)
    print("The least costed Sunscreen SPF-50 Product is: ",sunscreen_sp5_50_product_with_min_price.text)
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value).click()

def add_SPF_30_product_with_least_price_to_cart(driver):
    "This function extracts only the SPF-30 products and adds the least priced SPD-30 product to the cart"
    spf_30_price=[]
    sunscreen_spf_30_products=driver.find_elements_by_xpath("//p[contains(text(),'SPF-30') or contains(text(),'spf-30')]/following-sibling::p")
    for each_element in sunscreen_spf_30_products:  
        price=int(each_element.text.split()[-1])
        spf_30_price.append(price)
    print("The list of of Sunscreen price which belongs to SPF-30 are: ",spf_30_price)
    min_value=10000
    for item in spf_30_price:
        if item<min_value:
            min_value=int(item)
    print("The least priced Sunscreen SPF-30 value is: ",min_value)
    sunscreen_sp5_30_product_with_min_price=driver.find_element_by_xpath("//p[contains(text(),'%d')]/parent::div/p[contains(text(),'SPF-30')]"%min_value).text
    print("The least costed Sunscreen SPF-30 Product is: ",sunscreen_sp5_30_product_with_min_price)
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value).click()

def close_webpage():
    "This function closes the browser"
    driver.quit()

def click_cart():
    "This funcion will navigate to cart screen and takes a screenshot"
    driver.find_element_by_xpath("//span[@id='cart']").click()
    driver.save_screenshot("cart.png")

if __name__ == "__main__":
    #This calling function will launch the webpage and navigates to the provided url.
    launch_webpage()
    time.sleep(2)

    #This calling function will add the least priced SPF_50_product to the cart.
    add_SPF_50_product_with_least_price_to_cart(driver)

    #This calling function will add the least priced SPF_30_product to the cart.
    add_SPF_30_product_with_least_price_to_cart(driver)

    #This calling function will click on the cart button so that we can view the cart items.
    click_cart()

    #This calling function will close the browser.
    close_webpage()

    