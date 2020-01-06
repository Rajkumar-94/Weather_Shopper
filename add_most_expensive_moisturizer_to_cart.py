"""
The script is an example of weather shopper
This Selenium Python code will selects the most expensive Moistuzier product and adds it to the cart and takes the screenshot of the added Product

"""


from selenium import webdriver
import time

def launch_webpage():
    "This function launches the website and navigates the provided URL"
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

def add_expensive_product_to_cart():
    "This function extracts the price of each product, take selects the expensive value, prints the expensive item name and add it to the cart"
    price_list=[]
    products=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")
    for item in products:  
        price=int(item.text.split()[-1])
        price_list.append(price)
    print("The list of of Sunscreen products price are: ",price_list)
    price_list.sort()
    most_expensive=price_list[-1]
    expensive_product=driver.find_element_by_xpath("//p[contains(text(),'%d')]/parent::div/p[@class='font-weight-bold top-space-10']"%most_expensive).text
    print("The expensive product is %s "%expensive_product, "and the price is %d"%most_expensive)
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%most_expensive).click()

def click_on_cart():
    #This function will clcik and take screenshot of the products added to the cart.
    driver.find_element_by_xpath("//span[@id='cart']").click()
    driver.save_screenshot("screenshot.png")

def close_webpage():
    "This function closes the browser"
    driver.close()

if __name__ == "__main__":
    #This calling function will launch the webpage and navigates to the provided url.
    launch_webpage()
    time.sleep(2)

    #This calling function will add the expensive moisturizer product to the cart.
    add_expensive_product_to_cart()

    #This calling function will clcik and take screenshot of the products added to the cart.
    click_on_cart()

    #This calling function will close the browser.
    close_webpage()

