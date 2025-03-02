from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the registration page
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
driver.maximize_window()
time.sleep(2)

# Fill in the registration form
username = driver.find_element(By.ID, "input-firstname")
username.send_keys("John")
lastname = driver.find_element(By.ID, "input-lastname")
lastname.send_keys("Doe")
email = driver.find_element(By.ID, "input-email")
email.send_keys("123@gnnail.com")
telephone = driver.find_element(By.ID, "input-telephone")
telephone.send_keys("1234567890")
password = driver.find_element(By.ID, "input-password")
password.send_keys("password")
confirm_password = driver.find_element(By.ID, "input-confirm")
confirm_password.send_keys("password")

# Subscribe to the newsletter
newsletter_subscribe = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/div')
newsletter_subscribe.click()

# Agree to the terms and conditions
# agree = driver.find_element(By.NAME, 'agree')
# agree.click()

# Submit the form
continue_button = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input')
continue_button.click()

# Wait for the success message or redirection to the account page
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/h1'))
    )
    print("Registration successful!")
except Exception as e:
    print("Registration failed or took too long.")
    print(e)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight + 200);")
time.sleep(20)

# Keep the browser open for a longer period
time.sleep(60)  # Adjust the time as needed


# Close the browser
driver.quit()