# MCP Server Selenium Playwright QA

This repository contains automation scripts and examples for testing web applications using Selenium and Playwright with MCP (Model Context Protocol) servers.

## 📁 Project Structure

### Module01_Automation_UsingPlaywright
- **VWO Invalid Login Test**: Python Playwright automation for testing invalid login functionality
- **Lab Files**: Documentation and prompts for Playwright automation tasks

### Module02_Automation_UsingSelenium
- **VWO Invalid Login Test**: Java and Python Selenium automation for testing invalid login functionality
- **iDrive360 Signup Test**: Selenium automation for testing signup process with error validation
- **Screenshots**: Test execution screenshots captured during automation runs

### Module03_Push_Code_To_GitHub
- **GitHub Integration**: Documentation for pushing code to GitHub repositories

### Module04_Generate_Automation_Script
- **Code Generation**: Python and Java automation scripts for various testing scenarios

## 🚀 Features

- **Cross-Platform Automation**: Support for both Selenium and Playwright frameworks
- **Multiple Languages**: Python and Java implementations
- **MCP Integration**: Model Context Protocol server integration for AI-powered automation
- **Screenshot Capture**: Automatic screenshot capture during test execution
- **Error Handling**: Comprehensive error handling and validation
- **Random Data Generation**: Dynamic test data generation for realistic testing

## 🛠️ Technologies Used

- **Selenium WebDriver**: Web automation framework
- **Playwright**: Modern web automation framework
- **Python**: Primary scripting language
- **Java**: Alternative implementation language
- **MCP (Model Context Protocol)**: AI integration protocol
- **Git**: Version control
- **GitHub**: Repository hosting

## 📋 Test Scenarios

### VWO Invalid Login Testing
- Tests invalid login functionality
- Verifies error message display
- Captures screenshots of error states
- Supports both Selenium and Playwright

### iDrive360 Signup Testing
- Tests signup form validation
- Includes country code selection
- Phone number validation
- Form field error handling

## 🏃‍♂️ Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AuTeLipi/MCP_Server_Selenium_Playwright_QA.git
   cd MCP_Server_Selenium_Playwright_QA
   ```

2. **Install dependencies**:
   ```bash
   # For Python scripts
   pip install selenium playwright
   playwright install
   
   # For Java scripts
   # Add Selenium WebDriver dependencies to your project
   ```

3. **Run tests**:
   ```bash
   # Python Playwright
   python Module01_Automation_UsingPlaywright/vwo_invalid_login_test.py
   
   # Python Selenium
   python Module02_Automation_UsingSelenium/vwo_invalid_login_selenium.py
   
   # Java Selenium
   javac -cp "selenium-java.jar" Module02_Automation_UsingSelenium/VWOInvalidLoginSelenium.java
   java -cp ".:selenium-java.jar" VWOInvalidLoginSelenium
   ```

## 📸 Screenshots

The repository includes screenshots from test executions showing:
- Initial page loads
- Form filling processes
- Error message displays
- Final test results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Author

**AuTeLipi** - [GitHub Profile](https://github.com/AuTeLipi)

## 📞 Support

For support and questions, please open an issue in the GitHub repository.
