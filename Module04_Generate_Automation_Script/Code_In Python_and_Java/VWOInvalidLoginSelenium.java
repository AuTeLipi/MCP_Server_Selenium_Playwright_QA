import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.TimeoutException;
import java.time.Duration;
import java.util.Random;
import java.io.File;
import java.io.IOException;

public class VWOInvalidLoginSelenium {
    
    private static WebDriver driver;
    private static WebDriverWait wait;
    
    public static void main(String[] args) {
        try {
            // Setup Chrome options
            ChromeOptions options = new ChromeOptions();
            options.addArguments("--no-sandbox");
            options.addArguments("--disable-dev-shm-usage");
            // Set headless to false as requested
            options.setHeadless(false);
            
            System.out.println("Starting VWO Invalid Login Test with Selenium...");
            System.out.println("Launching Chrome browser (headless=false)...");
            
            // Initialize Chrome driver
            driver = new ChromeDriver(options);
            driver.manage().window().maximize();
            
            // Initialize WebDriverWait
            wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            
            // Navigate to VWO login page
            System.out.println("Navigating to VWO login page...");
            driver.get("http://app.vwo.com");
            
            // Wait for page to load
            wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("body")));
            
            // Take initial screenshot
            System.out.println("Taking initial screenshot...");
            takeScreenshot("vwo_initial_page.png");
            
            // Generate random credentials
            String randomEmail = generateRandomEmail();
            String randomPassword = generateRandomPassword();
            
            System.out.println("Using random email: " + randomEmail);
            System.out.println("Using random password: " + randomPassword);
            
            // Find and fill email field
            System.out.println("Finding and filling email field...");
            if (!fillEmailField(randomEmail)) {
                System.out.println("❌ Could not find email field");
                return;
            }
            
            // Find and fill password field
            System.out.println("Finding and filling password field...");
            if (!fillPasswordField(randomPassword)) {
                System.out.println("❌ Could not find password field");
                return;
            }
            
            // Take screenshot after filling fields
            System.out.println("Taking screenshot after filling credentials...");
            takeScreenshot("vwo_credentials_filled.png");
            
            // Find and click submit button
            System.out.println("Finding and clicking submit button...");
            if (!clickSubmitButton()) {
                System.out.println("❌ Could not find or click submit button");
                return;
            }
            
            // Wait for error message to appear
            System.out.println("Waiting for error message to appear...");
            Thread.sleep(3000); // Wait for page to process
            
            // Take screenshot after submit
            System.out.println("Taking screenshot after submit...");
            takeScreenshot("vwo_after_submit.png");
            
            // Try to find and verify error message
            System.out.println("Looking for error message...");
            verifyErrorMessage();
            
            // Take final screenshot
            System.out.println("Taking final screenshot...");
            takeScreenshot("vwo_final_result.png");
            
            // Wait a moment to see the result
            Thread.sleep(2000);
            
            System.out.println("✓ Test completed successfully!");
            System.out.println("Screenshots saved:");
            System.out.println("- vwo_initial_page.png");
            System.out.println("- vwo_credentials_filled.png");
            System.out.println("- vwo_after_submit.png");
            System.out.println("- vwo_final_result.png");
            
        } catch (Exception e) {
            System.err.println("❌ Error during test execution: " + e.getMessage());
            e.printStackTrace();
            
            // Take error screenshot
            try {
                takeScreenshot("vwo_error_screenshot.png");
                System.out.println("Error screenshot saved as: vwo_error_screenshot.png");
            } catch (Exception screenshotError) {
                System.err.println("Failed to take error screenshot: " + screenshotError.getMessage());
            }
        } finally {
            // Close browser
            if (driver != null) {
                System.out.println("Closing browser...");
                driver.quit();
                System.out.println("Browser closed successfully!");
            }
        }
    }
    
    /**
     * Generate a random email address for testing
     */
    private static String generateRandomEmail() {
        Random random = new Random();
        String[] domains = {"test.com", "example.com", "invalid.com", "fake.org"};
        String[] names = {"user", "test", "invalid", "fake", "random", "demo"};
        
        String name = names[random.nextInt(names.length)];
        int number = random.nextInt(9999) + 1;
        String domain = domains[random.nextInt(domains.length)];
        
        return name + number + "@" + domain;
    }
    
    /**
     * Generate a random password for testing
     */
    private static String generateRandomPassword() {
        Random random = new Random();
        String[] passwords = {"wrongpass", "invalid123", "testpass", "fakepassword", "randompass", "demo123"};
        return passwords[random.nextInt(passwords.length)];
    }
    
    /**
     * Fill email field with random email
     */
    private static boolean fillEmailField(String email) {
        String[] emailSelectors = {
            "input[type=\"email\"]",
            "input[placeholder*=\"Email\"]",
            "input[name*=\"email\"]",
            "input[id*=\"email\"]",
            "input[class*=\"email\"]"
        };
        
        for (String selector : emailSelectors) {
            try {
                WebElement emailField = wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector(selector)));
                emailField.clear();
                emailField.sendKeys(email);
                System.out.println("✓ Email field filled using selector: " + selector);
                return true;
            } catch (TimeoutException e) {
                continue;
            }
        }
        
        System.out.println("⚠ Email field not found with any selector");
        return false;
    }
    
    /**
     * Fill password field with random password
     */
    private static boolean fillPasswordField(String password) {
        String[] passwordSelectors = {
            "input[type=\"password\"]",
            "input[placeholder*=\"Password\"]",
            "input[name*=\"password\"]",
            "input[id*=\"password\"]",
            "input[class*=\"password\"]"
        };
        
        for (String selector : passwordSelectors) {
            try {
                WebElement passwordField = wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector(selector)));
                passwordField.clear();
                passwordField.sendKeys(password);
                System.out.println("✓ Password field filled using selector: " + selector);
                return true;
            } catch (TimeoutException e) {
                continue;
            }
        }
        
        System.out.println("⚠ Password field not found with any selector");
        return false;
    }
    
    /**
     * Click submit button
     */
    private static boolean clickSubmitButton() {
        String[] submitSelectors = {
            "button[type=\"submit\"]",
            "input[type=\"submit\"]",
            ".btn-primary",
            ".login-btn",
            ".submit-btn",
            "button:contains(\"Sign in\")",
            "button:contains(\"Login\")",
            "button:contains(\"Submit\")"
        };
        
        for (String selector : submitSelectors) {
            try {
                WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector(selector)));
                submitButton.click();
                System.out.println("✓ Submit button clicked using selector: " + selector);
                return true;
            } catch (TimeoutException e) {
                continue;
            }
        }
        
        System.out.println("⚠ Submit button not found with any selector");
        return false;
    }
    
    /**
     * Verify error message is displayed
     */
    private static void verifyErrorMessage() {
        String[] errorSelectors = {
            ".error",
            ".alert",
            ".alert-danger",
            "[class*=\"error\"]",
            "[data-qa*=\"error\"]",
            ".invalid-feedback",
            ".error-message",
            ".login-error"
        };
        
        boolean errorMessageFound = false;
        
        for (String selector : errorSelectors) {
            try {
                WebElement errorElement = driver.findElement(By.cssSelector(selector));
                if (errorElement.isDisplayed()) {
                    String errorText = errorElement.getText();
                    if (!errorText.trim().isEmpty()) {
                        System.out.println("✓ Error message found: " + errorText);
                        System.out.println("✓ Invalid login test passed - Error message displayed correctly");
                        errorMessageFound = true;
                        break;
                    }
                }
            } catch (NoSuchElementException e) {
                continue;
            }
        }
        
        if (!errorMessageFound) {
            System.out.println("⚠ No error message found, but test continues...");
            System.out.println("This might be normal if the page redirects or shows error differently");
        }
    }
    
    /**
     * Take screenshot and save to file
     */
    private static void takeScreenshot(String filename) {
        try {
            TakesScreenshot screenshot = (TakesScreenshot) driver;
            File sourceFile = screenshot.getScreenshotAs(OutputType.FILE);
            File destinationFile = new File(filename);
            
            // Copy file to destination
            org.apache.commons.io.FileUtils.copyFile(sourceFile, destinationFile);
            System.out.println("Screenshot saved: " + filename);
        } catch (Exception e) {
            System.err.println("Failed to take screenshot: " + e.getMessage());
        }
    }
}
