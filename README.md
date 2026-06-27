# E2E Automation Testing Project - QA Playground Bank

This project implements a robust End-to-End (E2E) automation testing framework for the dynamic banking application **QA Playground - Bank**. 
The architecture strictly follows industry best practices, utilizing the **Page Object Model (POM)** design pattern, achieving complete separation between the test layer and UI/logic layer, and handling dynamic element locators and state synchronization asynchronously.

## 🎯 Test Coverage
The framework consists of independent, atomic test scenarios designed to validate the full lifecycle of account management and financial transactions:
* **Sanity & Initial Balance Verification:** Validates successful page loading and ensures the initial account balance is correctly loaded and greater than 0.
* **Cash Withdrawal Flow:** * **Success:** Verifies a successful withdrawal and asserts that the precise amount is deducted from the total balance.
  * **Insufficient Funds:** Validates the system's edge-case handling when attempting to withdraw more than the available balance, verifying that the appropriate error alert is displayed.
* **Cash Deposit Flow:** Validates depositing money into the account and confirms that the total balance reflects the update accurately.
* **Account-to-Account Transfers:**
  * **Primary to Secondary Account:** Verifies transferring funds from the Primary Savings account to the Checking account.
  * **Secondary to Primary Account:** Verifies transferring funds back from the Checking account to the Primary Savings account, successfully handling dynamic, conditional dropdown fields and updating specific account balances.

## 🛠️ Tech Stack & Dependencies
* **Python 3.x**
* **Playwright (Python)** 
* **Pytest** 
* **Pytest-html** 


Setup & Execution Guide
1. Environment Setup & Installation
Open your terminal in the project's root directory and run the following commands:

Activate the Virtual Environment (venv1):

On Windows:
venv1\Scripts\activate

On Mac/Linux:
source venv1/bin/activate

Install Python Dependencies:
pip install -r requirements.txt

Install Required Playwright Browser Binaries:
playwright install

2. Running the Tests
You can execute the entire suite together or target specific feature files individually depending on your testing scope.

To run the entire test suite sequentially:
pytest

To run specific test modules independently:

Authentication/Login Tests:
pytest ./tests/test_login.py

Session/Logout Tests:
pytest ./tests/test_logout.py

Core Account Dashboard & Transaction Tests:
pytest ./tests/test_dashboard.py

📊 Viewing the Test Report
The framework is pre-configured via pytest.ini to automatically generate a rich, standalone HTML visual report upon execution completion. You can open it in any web browser:

Report Path: reports/report.html