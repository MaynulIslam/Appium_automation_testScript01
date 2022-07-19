import base64
import time
import unittest
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


desired_cap ={
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "appPackage": "com.nopstation.nopcommerce.nopstationcart",
    "appActivity": "com.bs.ecommerce.main.SplashScreenActivity",
    "app": "C:\\Users\\Maynul\\Desktop\\SQA R&D\\nopstationcart\\nopstationCart_4.40.apk"
}

#create driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)

#Start recording
#driver.start_recording_screen()

# click on the accept and agree

#driver.find_element_by_id("com.nopstation.nopcommerce.nopstationcart:id/btnAccept").click()

driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button').click()
driver.implicitly_wait(15)

driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="NopStation Cart"]').click()
driver.implicitly_wait(15)

driver.find_element(By.XPATH,'(//android.widget.ImageView[@content-desc="Placeholder"])[4]').click()
driver.implicitly_wait(15)

#search
driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="Search"]/android.widget.FrameLayout/android.widget.ImageView').click()
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/search_src_text').send_keys('Nokia Lumia 1020')
driver.implicitly_wait(3)


#driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/searchView').click()
#driver.implicitly_wait(5)

driver.execute_script('mobile: performEditorAction', {'action': 'search'})
driver.implicitly_wait(15)

#click to the product

driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/ivAddToFav').click()
driver.implicitly_wait(10)

#driver.set_value(00000000-0000-018e-ffff-ffff00000190 = 'Nokia Lumia 1020')

"""
Touch to up
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(522, 1652)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(533, 1031)
actions.w3c_actions.pointer_action.release()
actions.perform()

"""
touch = TouchAction(driver)
touch.press(x=1232, y=1964).move_to(x=1244, y=603).release().perform()
time.sleep(3)

for i in range(1):
    touch = TouchAction(driver)
    touch.press(x=1232, y=1964).move_to(x=1244, y=603).release().perform()
    time.sleep(3)


#select size "Large"
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[3]').click()
driver.implicitly_wait(3)

driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[2]').click()
driver.implicitly_wait(3)

driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/tvDone').click()
driver.implicitly_wait(3)

#increase Qty by "2"
driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnPlus').click()
driver.implicitly_wait(3)
#add to cart button to add the product in his cart
driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnAddToCart').click()
driver.implicitly_wait(3)

                                # Scenario: 02 Customer successfully place order as a guest user

#go to shopping cart by clicking top cart icon
driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/counterIcon').click()

driver.implicitly_wait(3)
#click checkout button from shopping cart page
driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnCheckOut').click()
driver.implicitly_wait(3)

#checkout as guest from shopping cart page
driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout').click()
driver.implicitly_wait(3)

#input all the details in checkout billing details page and click continue

 # frist name, last name and Email**
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etFirstName').send_keys('Mike')
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etLastName').send_keys('sandwich')
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etEmail').send_keys('milesandwich@gmail.com')
driver.implicitly_wait(5)

"""
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1052, 1228)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(1034, 621)
actions.w3c_actions.pointer_action.release()
actions.perform()
    

    
"""
#scroll for better view of select country
touch = TouchAction(driver)
touch.press(x=1163, y=1673).move_to(x=1159, y=1044).release().perform()
time.sleep(3)

driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/countrySpinner').click()
driver.implicitly_wait(5)

touch = TouchAction(driver)
touch.press(x=1305, y=2052).move_to(x=1301, y=1061).release().perform()
time.sleep(3)

for i in range(2):
    touch = TouchAction(driver)
    touch.press(x=1305, y=2052).move_to(x=1301, y=1061).release().perform()
    time.sleep(3)
driver.implicitly_wait(5)

driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[9]').click()
driver.implicitly_wait(3)

#Select State:
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/stateSpinner').click()
driver.implicitly_wait(3)

driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]').click()
driver.implicitly_wait(3)

#company
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etCompanyName').send_keys('XYZ Corporation.')

#try again to scroll
touch = TouchAction(driver)
touch.press(x=1387, y=2109).move_to(x=1379, y=775).release().perform()
time.sleep(3)

for i in range(1):
    touch = TouchAction(driver)
    touch.press(x=1387, y=2109).move_to(x=1379, y=775).release().perform()
    time.sleep(3)


#company, city, street address, zip code and phone number
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etCity').send_keys('Dhaka')
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress').send_keys('94/7, North kafrul, Dhaka cantonment')
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etZipCode').send_keys('1206')
driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/etPhone').send_keys('+88 0123361255')

#again scroll to get to the Continue buttor

"""
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1052, 1839)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(1041, 1204)
actions.w3c_actions.pointer_action.release()
actions.perform()
"""

touch = TouchAction(driver)
touch.press(x=1052, y=1839).move_to(x=1041, y=1204).release().perform()
time.sleep(3)

for i in range(1):
    touch = TouchAction(driver)
    touch.press(x=1052, y=1839).move_to(x=1041, y=1204).release().perform()
    time.sleep(1)

driver.find_element(By.ID,'com.nopstation.nopcommerce.nopstationcart:id/btnContinue').click()
driver.implicitly_wait(3)


#click next day
driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[4]').click()
driver.implicitly_wait(2)

#scroll on shipping page

touch = TouchAction(driver)
touch.press(x=1424, y=2060).move_to(x=1420, y=689).release().perform()
time.sleep(3)

for i in range(1):
    touch = TouchAction(driver)
    touch.press(x=1424, y=2060).move_to(x=1420, y=689).release().perform()
    time.sleep(3)

#click continue
driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
driver.implicitly_wait(5)

#"Check/Money Order"
touch = TouchAction(driver)
touch.press(x=1420, y=2121).move_to(x=1416, y=592).release().perform()
time.sleep(3)

for i in range(4):
    touch = TouchAction(driver)
    touch.press(x=1420, y=2121).move_to(x=1416, y=592).release().perform()
    time.sleep(3)


driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]').click()
driver.implicitly_wait(5)

#Click_continue
driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
driver.implicitly_wait(5)

#click on the next button
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button').click()
driver.implicitly_wait(3)

#confirm button to place the order
driver.find_element(By.ID, 'com.nopstation.nopcommerce.nopstationcart:id/btnContinue').click()
driver.implicitly_wait(15)

# assertion test


#recoding stop
"""
video_rawdata = driver.stop_recording_screen()

video_name = driver.current_activity + time.struct_time("%Y_%m_%d_%H%M%S")

filepath = os.path.join("", video_name+".mp4")

with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))
"""

