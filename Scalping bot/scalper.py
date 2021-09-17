from logging import RootLogger
from sys import path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound

login_user = "JohnDoe@gmail.com"        # Enter user here
password_user = "password"              # Enter password here
paypal_user = "JaneDoe@gmail.com"       # Paypal login
paypal_password = "different password"  # Paypal password

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/sshao/AppData/Local/Google/Chrome/User Data') # yeah its gonna be a bit more work to sell this as a product
options.add_argument('--profile-directory=Profile 1')

browser = webdriver.Chrome('C:\webdrivers\chromedriver', options=options)
# Bestbuy EVGA RTX 3080 XC3 page
# browser.get("https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-video-card/15084753")

# bestbuy sign in
browser.get("https://www.bestbuy.ca/identity/en-ca/signin?tid=9KPOTpx6dzFmu2MzAZPJn8hcx1Z3MTVXQMAtaUlnX4CYrHwj%252Fm%252FT76VyJC%252FuoVv%252B1VAh%252BN%252FgeM3yM8x6LR%252FZ%252Bw%252B3WsyY%252BvW567mO4xtYcmio8LK5hLSp1SLJRUy3SZFsWgfpYWb3mJDdrtXheWQOG7uBkXc0OzDwL0wKObNgiS8aYYukAauxJiAiPnw8n0p%252Br8w2IsCjAtV711u2UNUrlOjtO%252B2qSZxN%252Fl1S0ovQ5QcLpMAHhnJSnZTIMNM9El6682lk1pA%252B83BZKUeTSg7QMEE5myovTcqI5bZTAgTfjRqK6rCZ5SYIlj3BMr9knGJW")

# Fill in login
login = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/fieldset/div[1]/div/div[1]/div/input")
login.clear()
login.send_keys(login_user)

# Fill in Password
password = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/fieldset/div[2]/div/div[1]/div/input")
password.clear()
password.send_keys(password_user)

# Sign in
signinbutton = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/div/button")
signinbutton.click()

try:
    element = WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/header/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/a"))
    )

# cart button
finally:
    print("Cart button loaded")
cart_button = browser.find_element_by_xpath("/html/body/div/div/header/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/a")
cart_button.click()


# bestbut click cart icon
time.sleep(5)
buyButton = False

while not buyButton:
    try:
        #If this works then button is not ready
        continue_shopping = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[2]/section/div/main/section/div/a")

        # Button isnt open restart script
        print("Button is not ready yet.")

        # Refresh browser
        time.sleep(1)
        print("wait.")
        browser.refresh
    
    except:
        paypal_checkout = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[2]/section/div/main/section/section[2]/div[4]/div[1]/div/div/a")
        playsound(r"C:\Users\sshao\Desktop\Scalping bot\ohyeah.mp3")
        #Click the button 
        print("Button was clicked.")
        paypal_checkout.click()
        buyButton = True

try:
    element = WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]/div[2]/div[1]/input"))
    )
finally:
    print("Paypal login screen loaded")

# Paypal login:
paypal_login = browser.find_element_by_xpath("/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]/div[2]/div[1]/input")
paypal_login.clear()
paypal_login.send_keys(paypal_user)

# Fill in Password
paypal_password = browser.find_element_by_xpath("/html/body/div[1]/section[1]/div/div/form/div[1]/div[2]/div/div[1]/input")
paypal_password.clear()
paypal_password.send_keys(paypal_password)

# Paypal Sign in
paypal_signin = browser.find_element_by_xpath("/html/body/div[1]/section[1]/div/div/form/div[2]/button")
paypal_signin.click()

# Agree and continue
paypal_agree_and_continue = browser.find_element_by_xpath("/html/body/div[1]/div/div/main/div[8]/div/button")
paypal_agree_and_continue.click()