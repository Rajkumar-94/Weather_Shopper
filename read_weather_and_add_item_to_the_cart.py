from selenium import webdriver
import time

def launch_webpage():
    global driver
    driver = webdriver.Chrome()
    # Maximize the browser window
    driver.maximize_window()
    # Navigate to Qxf2 Tutorial page
    driver.get("https://weathershopper.pythonanywhere.com/")
    time.sleep(3)
    temperature=driver.find_element_by_xpath("//span[@id='temperature']").text
    temp=int(temperature.split()[0])
    print("The Temperature is: ",temp)
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
    

launch_webpage()