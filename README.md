<div align="center">

# 🤖 MCP Server: Selenium + Playwright QA Automation

### *Unified Web Testing MCP Servers for AI-Driven Browser Automation*

![Testing Status](https://img.shields.io/badge/Testing-Automated-brightgreen?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge)
![Framework](https://img.shields.io/badge/Multi--Framework-Selenium%20%7C%20Playwright-orange?style=for-the-badge)

*Revolutionizing QA workflows with Model Context Protocol integration*

[🚀 Quick Start](#-launch-sequence) • [🎯 Features](#-arsenal-features) • [📖 Documentation](#-battle-plans) • [🤝 Contribute](#-join-the-mission)

![Image](https://github.com/user-attachments/assets/a42f74e6-e3cb-4495-98fe-edf57d81f783)

</div>


---


## 🌐 **Project Overview**
This project demonstrates how to orchestrate web-testing MCP (Model Context Protocol) servers (Selenium MCP and Playwright MCP) from a unified QA workspace, enabling AI agents to drive real browsers through natural language commands in modern IDEs like **Cursor/VS Code** or AI clients like **Claude Desktop** and **Goose**.

**Why MCP for QA?**
- 🛠️ **Standardized Interface**: Consistent API for AI agents across different automation frameworks
- 👨‍💻 **Developer-Centric Workflow**: Transform natural language prompts into executable test code instantly
- 🔄 **Framework Agnostic**: Seamlessly switch between Selenium and Playwright without changing your approach
- 🎯 **IDE Integration**: Native support in modern development environments

## 🎭 **The Evolution of Testing**

Gone are the days of writing hundreds of lines of boilerplate automation code. **MCP QA Automation** represents the next evolution in software testing—where AI agents understand your testing intent and translate it into precise browser actions across multiple frameworks.

### 🌟 **What Makes Us Different?**

Unlike traditional automation tools that require extensive coding knowledge, our MCP-integrated approach allows you to:
- **Speak in Plain English**: Describe your test scenarios naturally
- **Instant Code Generation**: Watch AI transform your ideas into executable tests  
- **Cross-Framework Harmony**: Seamlessly switch between Selenium and Playwright
- **Visual Intelligence**: AI-powered element recognition and interaction

---

## 🎯 **Arsenal Features**

### 🔮 **AI-Powered Test Generation**
```bash
# Simply describe what you want to test
"Test the login with invalid credentials and capture the error message"
# → Generates complete test automation code
```

### 🎨 **Multi-Framework Architecture**
| Framework | Language | Strengths |
|-----------|----------|-----------|
| **Playwright** 🎭 | Python | Modern, fast, reliable |
| **Selenium** 🕸️ | Java & Python | Industry standard, extensive support |

### 🎪 **Smart Test Scenarios**
- **🔐 Authentication Testing**: Login/logout flows with intelligent error detection
- **📋 Form Validation**: Dynamic form testing with real-time feedback
- **📱 Cross-Browser Compatibility**: One test, multiple browsers
- **📸 Visual Regression**: Automated screenshot comparison

---

## 🚀 **Launch Sequence**

### **Step 1: Clone the Arsenal**
```bash
git clone https://github.com/AuTeLipi/MCP_Server_Selenium_Playwright_QA.git
cd MCP_Server_Selenium_Playwright_QA
```

### **Step 2: Prepare Your Weapons**
```bash
# Python Environment
pip install -r requirements.txt
playwright install

# Java Environment (for Selenium)
# Ensure Java 11+ and Maven are installed
```

### **Step 3: Configure MCP Integration**
Create `.cursor/mcp.json` in your IDE:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "selenium": {
      "command": "npx", 
      "args": ["-y", "@angiejones/mcp-selenium"]
    }
  }
}
```

### **Step 4: Launch Your First Mission**
```bash
# Playwright Mission
python Module01_Automation_UsingPlaywright/vwo_invalid_login_test.py

# Selenium Mission  
python Module02_Automation_UsingSelenium/vwo_invalid_login_selenium.py
```

---

## 🗂️ **Mission Control Structure**

```
🏗️ MCP_Server_Selenium_Playwright_QA/
├── 🎭 Module01_Automation_UsingPlaywright/
│   ├── 🎯 vwo_invalid_login_test.py
│   └── 📚 lab_guides/
├── 🕸️ Module02_Automation_UsingSelenium/
│   ├── ☕ Java_implementations/
│   ├── 🐍 Python_implementations/
│   └── 📸 execution_screenshots/
├── 🐙 Module03_Push_Code_To_GitHub/
│   └── 🔄 integration_guides/
├── ⚡ Module04_Generate_Automation_Script/
│   ├── 🤖 ai_generated_scripts/
│   └── 📋 templates/
└── ⚙️ Configuration/
    ├── mcp.json
    └── requirements.txt
```

---

## 🧪 **Live Experiments**

### 🔬 **Test Case: VWO Login Validation**
**Objective**: Validate error handling for invalid login attempts

**AI Prompt**: *"Create a test that tries to login with wrong credentials on VWO and verifies the error message"*

**Generated Output**:
- ✅ Automated browser launch
- ✅ Form interaction simulation  
- ✅ Error message capture
- ✅ Screenshot documentation
- ✅ Assertion validation

### 🔬 **Test Case: iDrive360 Signup Flow**
**Objective**: Test comprehensive signup form validation

**Results**:
- 📱 Country code selection testing
- 📞 Phone number format validation
- ⚠️ Real-time error feedback capture
- 📊 Form completion analytics

---

## 🎨 **Visual Chronicles**

Our tests don't just pass/fail—they tell stories through captured moments:

| Test Phase | Visual Evidence |
|------------|----------------|
| 🏁 **Initial Load** | Clean page state capture |
| ⌨️ **User Interaction** | Form filling progression |
| ❌ **Error States** | Validation message display |
| 🎯 **Final Results** | Success/failure documentation |

---

## 🔧 **Advanced Configuration**

### **Custom Test Data Factory**
```python
# Dynamic data generation for realistic testing
class TestDataFactory:
    @staticmethod
    def generate_invalid_credentials():
        return {
            "username": fake.email(),
            "password": fake.password(length=8),
            "expected_error": "Your email, password, IP address or location did not match"
        }
```

### **Multi-Environment Support**
```yaml
# environments.yml
staging:
  base_url: "https://staging.vwo.com"
  timeout: 10000
  
production:
  base_url: "https://vwo.com"
  timeout: 5000
```

---

## 🤝 **Join the Mission**

### **For Contributors**
1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch (`feature/amazing-test-case`)
3. ✨ **Commit** your changes with descriptive messages
4. 🚀 **Push** to your branch
5. 🎯 **Create** a Pull Request with detailed description

### **For Testers**
- 🐛 Report bugs with detailed reproduction steps
- 💡 Suggest new test scenarios
- 📝 Improve documentation
- 🎨 Share creative test implementations

---

## 🏆 **Hall of Fame**

### **Created By**
**[AuTeLipi](https://github.com/AuTeLipi)** - *The Architect of Automated Excellence*

### **Special Thanks**
- **Pramod Dutta** for introducing MCP and opening new horizons in test automation
- **Microsoft Playwright Team** for MCP integration
- **Angie Jones** for Selenium MCP development
- The **QA Community** for continuous inspiration

---

## 📜 **License & Disclaimer**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

*Built with ❤️ for the QA community. May your tests be green and your bugs be few.*

---

<div align="center">

### **Ready to revolutionize your testing workflow?**

[![Star this repo](https://img.shields.io/badge/⭐-Star%20This%20Repo-yellow?style=for-the-badge)](https://github.com/AuTeLipi/MCP_Server_Selenium_Playwright_QA)
[![Follow for updates](https://img.shields.io/badge/👨‍💻-Follow%20for%20Updates-blue?style=for-the-badge)](https://github.com/AuTeLipi)

**The future of testing is here. Are you ready to embrace it?**

</div>
