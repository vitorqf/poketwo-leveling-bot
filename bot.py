import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Your email and password goes here
email = "email"
password = "password"

# Starts chrome session
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options
)

redirect_to = "?redirect_to=%2Fchannels%2F312647855636742144%2F1099453146138423327"

driver.get(f"https://discord.com/login{redirect_to}")

time.sleep(6)


# When page is ready it will fill the email and password fields and click on login button
username_input = driver.find_element(By.NAME, "email")
username_input.send_keys(email)


password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)


login_button = driver.find_element(
    By.XPATH,
    '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]',
)
login_button.click()

time.sleep(6)

# How many times you want bot to spam
x = 100000000
i = 0

while i < x:
    try: 
 
        time.sleep(1)

        # Click on anti-spam button when it appears
        try:
            anti_spam_button = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/form/div[2]/button",
            )
            anti_spam_button.click()

            

            time.sleep(5)

            msg_input = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/main/form/div/div[1]/div/div[3]/div/div",
            )
            msg_input.send_keys("*")
            msg_input.send_keys(Keys.ENTER)

        except:
            pass

        # Starts here
        try:
            msg_input = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]",
            )

            msg_input.send_keys("*")
            msg_input.send_keys(Keys.ENTER)

        except:
            pass

        i += 1
        print('Messages sent: ', i)

    except(KeyboardInterrupt, SystemExit):
        print("Interrupted")
        driver.close()
        driver.quit()
        exit() 
    