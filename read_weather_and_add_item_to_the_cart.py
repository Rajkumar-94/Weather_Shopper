from selenium import webdriver
import time

def launch_webpage():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/")
    time.sleep(3)
    
def get_climate_temperature():    
    temperature=driver.find_element_by_xpath("//span[@id='temperature']").text
    global temp
    temp=int(temperature.split()[0])
    print("The Temperature is: ",temp)

def choose_product_based_on_climate():
    if temp<19:
        driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
        time.sleep(2)

        if(driver.title=="The Best Moisturizers in the World!"):
            print("Successly choosed Moistursizers based on the climate")
        else:
            print("Fail:Did not navigated to Moistursizers page")

    elif temp>34:
        driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
        time.sleep(2)
        if(driver.title=="The Best Sunscreens in the World!"):
            print("Successly navigated to Sunscreens page based on the climate")
        else:
            print("Fail:Did not navigated to Sunscreens page")

def close_webpage():
    driver.quit()

if __name__ == "__main__":
    launch_webpage()
    get_climate_temperature()
    choose_product_based_on_climate()
    close_webpage()
