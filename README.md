# 🛠️ Automated Form Submission with Selenium  

## 🚀 Overview  
This Python script **automates the registration process** on an e-commerce website using **Selenium WebDriver**. It fills out the registration form, submits it, and verifies whether the registration was successful.

📌 **Website Used for Testing:**  
[E-commerce Playground](https://ecommerce-playground.lambdatest.io/index.php?route=account/register)

---

## 🏗️ Features  
✅ Opens the **registration page** in Chrome  
✅ Fills in the **user details** (first name, last name, email, phone, password)  
✅ Selects **newsletter subscription**  
✅ Submits the form  
✅ Waits for a **success message** after registration  
✅ Scrolls the page to simulate user behavior  
✅ Keeps the browser open for debugging  

---

## 🛠️ Installation  

### 1️⃣ **Install Required Libraries**  
Make sure you have Python installed, then install dependencies:  

```bash
pip install selenium webdriver-manager
2️⃣ Download Chrome WebDriver (Auto)
The script automatically downloads the correct Chrome WebDriver version using webdriver-manager, so no manual setup is required.

▶️ Usage
Run the script with:


python formValidation_automate.py
This will open Chrome, navigate to the website, fill out the form, and submit it.

🏗️ How It Works
1️⃣ Setup WebDriver
The script uses webdriver-manager to automatically manage ChromeDriver.

2️⃣ Open the Registration Page

driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
3️⃣ Fill in User Details

username = driver.find_element(By.ID, "input-firstname")
username.send_keys("John")
4️⃣ Click on Subscribe to Newsletter & Submit Form

newsletter_subscribe = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/div')
newsletter_subscribe.click()
continue_button.click()
5️⃣ Verify Registration Success

success_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/h1'))
)
print("Registration successful!")
🛠️ Customization
🔹 Modify Input Fields:

Change username.send_keys("John") to any other name.
Update email, password, etc., in the script.
🔹 Enable Terms & Conditions Checkbox:

Uncomment the following line in the script if required:

agree = driver.find_element(By.NAME, 'agree')
agree.click()
🔹 Change the Browser:

You can modify the script to use Firefox or Edge instead of Chrome.
❗ Troubleshooting
🔹 Chrome Closes Too Fast?

Add this at the end of the script:

input("Press Enter to close the browser...")
🔹 Element Not Found?

Ensure the website structure hasn't changed.
Use time.sleep(2) before interacting with elements.
📜 License
This project is open-source and free to use.
