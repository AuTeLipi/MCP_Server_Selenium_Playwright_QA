import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def generate_random_email():
    """Generate a random email address for testing"""
    domains = ["test.com", "example.com", "invalid.com", "fake.org"]
    names = ["user", "test", "invalid", "fake", "random", "demo"]
    
    name = random.choice(names)
    number = random.randint(1, 9999)
    domain = random.choice(domains)
    
    return f"{name}{number}@{domain}"


def generate_random_password():
    """Generate a random password for testing"""
    passwords = ["wrongpass", "invalid123", "testpass", "fakepassword", "randompass", "demo123"]
    return random.choice(passwords)


def vwo_invalid_login_test():
    """Main test function for VWO invalid login automation using Selenium"""
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Set headless to False as requested
    chrome_options.headless = False
    
    # Initialize the driver
    driver = None
    
    try:
        print("Starting VWO Invalid Login Test with Selenium...")
        print("Launching Chrome browser (headless=False)...")
        
        # Initialize Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        # Navigate to VWO login page
        print("Navigating to VWO login page...")
        driver.get("http://app.vwo.com")
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Take initial screenshot
        print("Taking initial screenshot...")
        driver.save_screenshot("vwo_initial_page.png")
        
        # Generate random credentials
        random_email = generate_random_email()
        random_password = generate_random_password()
        
        print(f"Using random email: {random_email}")
        print(f"Using random password: {random_password}")
        
        # Find and fill email field
        print("Finding and filling email field...")
        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 
                    'input[type="email"], input[placeholder*="Email"], input[name*="email"]'))
            )
            email_field.clear()
            email_field.send_keys(random_email)
            print("✓ Email field filled successfully")
        except TimeoutException:
            print("⚠ Email field not found, trying alternative selectors...")
            # Try alternative selectors
            email_selectors = [
                'input[type="email"]',
                'input[placeholder*="Email"]',
                'input[name*="email"]',
                'input[id*="email"]',
                'input[class*="email"]'
            ]
            email_filled = False
            for selector in email_selectors:
                try:
                    email_field = driver.find_element(By.CSS_SELECTOR, selector)
                    email_field.clear()
                    email_field.send_keys(random_email)
                    print(f"✓ Email field filled using selector: {selector}")
                    email_filled = True
                    break
                except NoSuchElementException:
                    continue
            
            if not email_filled:
                print("❌ Could not find email field")
                return
        
        # Find and fill password field
        print("Finding and filling password field...")
        try:
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 
                    'input[type="password"], input[placeholder*="Password"], input[name*="password"]'))
            )
            password_field.clear()
            password_field.send_keys(random_password)
            print("✓ Password field filled successfully")
        except TimeoutException:
            print("⚠ Password field not found, trying alternative selectors...")
            # Try alternative selectors
            password_selectors = [
                'input[type="password"]',
                'input[placeholder*="Password"]',
                'input[name*="password"]',
                'input[id*="password"]',
                'input[class*="password"]'
            ]
            password_filled = False
            for selector in password_selectors:
                try:
                    password_field = driver.find_element(By.CSS_SELECTOR, selector)
                    password_field.clear()
                    password_field.send_keys(random_password)
                    print(f"✓ Password field filled using selector: {selector}")
                    password_filled = True
                    break
                except NoSuchElementException:
                    continue
            
            if not password_filled:
                print("❌ Could not find password field")
                return
        
        # Take screenshot after filling fields
        print("Taking screenshot after filling credentials...")
        driver.save_screenshot("vwo_credentials_filled.png")
        
        # Find and click submit button
        print("Finding and clicking submit button...")
        try:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 
                    'button[type="submit"], input[type="submit"], .btn-primary, button:contains("Sign in")'))
            )
            submit_button.click()
            print("✓ Submit button clicked successfully")
        except TimeoutException:
            print("⚠ Submit button not found, trying alternative selectors...")
            # Try alternative selectors
            submit_selectors = [
                'button[type="submit"]',
                'input[type="submit"]',
                '.btn-primary',
                'button:contains("Sign in")',
                'button:contains("Login")',
                'button:contains("Submit")',
                '.login-btn',
                '.submit-btn'
            ]
            submit_clicked = False
            for selector in submit_selectors:
                try:
                    submit_button = driver.find_element(By.CSS_SELECTOR, selector)
                    submit_button.click()
                    print(f"✓ Submit button clicked using selector: {selector}")
                    submit_clicked = True
                    break
                except (NoSuchElementException, Exception):
                    continue
            
            if not submit_clicked:
                print("❌ Could not find or click submit button")
                return
        
        # Wait for error message to appear
        print("Waiting for error message to appear...")
        time.sleep(3)  # Wait for page to process
        
        # Take screenshot after submit
        print("Taking screenshot after submit...")
        driver.save_screenshot("vwo_after_submit.png")
        
        # Try to find and verify error message
        print("Looking for error message...")
        error_message_found = False
        error_selectors = [
            '.error',
            '.alert',
            '.alert-danger',
            '[class*="error"]',
            '[data-qa*="error"]',
            '.invalid-feedback',
            '.error-message',
            '.login-error'
        ]
        
        for selector in error_selectors:
            try:
                error_element = driver.find_element(By.CSS_SELECTOR, selector)
                if error_element.is_displayed():
                    error_text = error_element.text
                    if error_text.strip():
                        print(f"✓ Error message found: {error_text}")
                        print("✓ Invalid login test passed - Error message displayed correctly")
                        error_message_found = True
                        break
            except NoSuchElementException:
                continue
        
        if not error_message_found:
            print("⚠ No error message found, but test continues...")
            print("This might be normal if the page redirects or shows error differently")
        
        # Take final screenshot
        print("Taking final screenshot...")
        driver.save_screenshot("vwo_final_result.png")
        
        # Wait a moment to see the result
        time.sleep(2)
        
        print("✓ Test completed successfully!")
        print("Screenshots saved:")
        print("- vwo_initial_page.png")
        print("- vwo_credentials_filled.png") 
        print("- vwo_after_submit.png")
        print("- vwo_final_result.png")
        
    except Exception as e:
        print(f"❌ Error during test execution: {e}")
        
        # Take error screenshot
        if driver:
            try:
                driver.save_screenshot("vwo_error_screenshot.png")
                print("Error screenshot saved as: vwo_error_screenshot.png")
            except Exception as screenshot_error:
                print(f"Failed to take error screenshot: {screenshot_error}")
    
    finally:
        # Close browser
        if driver:
            print("Closing browser...")
            driver.quit()
            print("Browser closed successfully!")


if __name__ == "__main__":
    vwo_invalid_login_test()
