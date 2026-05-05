Data Driven Testing Concepts
📌 Overview

This repository demonstrates the core concepts of Data-Driven Testing (DDT) using Python and Selenium.
It is a learning-focused implementation, where test data is stored externally (Excel) and used to drive test execution.

The project shows how to:

Read test data from Excel files
Perform automated login testing
Validate results (Pass/Fail)
Write results back into the Excel file

🧠 Key Concepts Covered

Data-Driven Testing (DDT)
External test data handling (Excel)
Read,Write and fill colour operations in Excel using utility class
Basic test validation (login success/failure)
Result logging back to test data file

📂 Project Structure

data_driven_testing_concepts/

│

├── XLUtilities.py        # Utility file for Excel operations

├── basic.py              # Basic data-driven example

├── login.py              # Instagram login test script

│

├── basic.csv             # test data write in this after basic.py ran.

├── login.csv             # Login test data (CSV)

├── basic.xlsx            # Sample Excel data

├── login-usha.xlsx       # Excel file with login credentials & results

⚙️ Features

🔹 XLUtilities.py:

Custom utility class created to handle Excel operations:
Read data from Excel
Write data to Excel
Fill cell with color (Hex format)

🔹 Login Automation (login.py):

Automates login functionality (Instagram)
Reads username & password from Excel (login-usha.xlsx)
Executes login using Selenium
Verifies login success or failure
Writes result back into Excel:
✅ Passed → Valid credentials
❌ Failed → Invalid credentials

🔹 Basic Data-Driven Script (basic.py):

Demonstrates simple read,write and fill colour operations.
Data is written in basic.xlxs file.

▶️ How It Works:
Test data (username & password) is stored in Excel file
Script reads data row by row
Selenium performs login operation
Result is validated
Output (Pass/Fail) is written back into Excel

🛠️ Tech Stack
Python
Selenium WebDriver
OpenPyXL
CSV Module

🚀 Purpose

This repository is created for learning and practicing Data-Driven Testing concepts, not as a production-level project.
It demonstrates how testers can:
Separate test data from test logic
Reuse test scripts with multiple datasets
Maintain test results efficiently

👩‍💻 Author

Usha Nazare
(Transitioning into Automation Testing | Python + Selenium)
