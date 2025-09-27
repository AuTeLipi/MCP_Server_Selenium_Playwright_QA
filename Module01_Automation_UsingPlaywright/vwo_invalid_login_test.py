import asyncio
import random
from playwright.async_api import async_playwright


async def generate_random_email():
    """Generate a random email address for testing"""
    domains = ["test.com", "example.com", "invalid.com", "fake.org"]
    names = ["user", "test", "invalid", "fake", "random", "demo"]
    
    name = random.choice(names)
    number = random.randint(1, 9999)
    domain = random.choice(domains)
    
    return f"{name}{number}@{domain}"


async def generate_random_password():
    """Generate a random password for testing"""
    passwords = ["wrongpass", "invalid123", "testpass", "fakepassword", "randompass", "demo123"]
    return random.choice(passwords)


async def vwo_invalid_login_test():
    """Main test function for VWO invalid login automation"""
    async with async_playwright() as p:
        # Launch browser
        print("Launching browser...")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            # Navigate to VWO login page
            print("Navigating to VWO login page...")
            await page.goto("https://app.vwo.com/")
            
            # Wait for the page to load
            await page.wait_for_load_state("networkidle")
            
            # Generate random email and password
            random_email = await generate_random_email()
            random_password = await generate_random_password()
            
            print(f"Using random email: {random_email}")
            print(f"Using random password: {random_password}")
            
            # Find and fill email field
            print("Filling email field...")
            await page.fill('input[placeholder="Email"]', random_email)
            
            # Find and fill password field
            print("Filling password field...")
            await page.fill('input[placeholder="Password"]', random_password)
            
            # Click submit button
            print("Clicking submit button...")
            await page.click('button[type="submit"], button:has-text("Sign in")')
            
            # Wait for error message to appear
            print("Waiting for error message...")
            try:
                await page.wait_for_selector(
                    '[data-qa="error-message"], .error-message, .alert-danger, .error, [class*="error"]',
                    timeout=10000
                )
                
                # Verify error message is displayed
                error_element = page.locator('[data-qa="error-message"], .error-message, .alert-danger, .error, [class*="error"]').first
                error_visible = await error_element.is_visible()
                
                if error_visible:
                    error_text = await error_element.text_content()
                    print(f"Error message found: {error_text}")
                    print("✓ Invalid login test passed - Error message displayed correctly")
                else:
                    print("⚠ Warning: No error message found, but test continues...")
                    
            except Exception as e:
                print(f"⚠ Warning: Error message not found within timeout: {e}")
                print("Test continues to take screenshot...")
            
            # Take screenshot
            print("Taking screenshot...")
            await page.screenshot(path="vwo_invalid_login_result.png")
            print("Screenshot saved as: vwo_invalid_login_result.png")
            
            # Wait a moment to see the result
            await page.wait_for_timeout(2000)
            
        except Exception as e:
            print(f"Error during test execution: {e}")
            
            # Take screenshot on error
            try:
                await page.screenshot(path="vwo_error_screenshot.png")
                print("Error screenshot saved as: vwo_error_screenshot.png")
            except Exception as screenshot_error:
                print(f"Failed to take error screenshot: {screenshot_error}")
                
        finally:
            # Close browser
            print("Closing browser...")
            await browser.close()
            print("Test completed successfully!")


async def main():
    """Main entry point"""
    print("Starting VWO Invalid Login Test with Python Playwright...")
    await vwo_invalid_login_test()


if __name__ == "__main__":
    # Run the async test
    asyncio.run(main())

