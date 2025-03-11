# Poll Sender

## Description
Poll Sender is a simple Python script that automates sending polls on WhatsApp Web. It opens WhatsApp Web, navigates to a specified group, and sends two predefined polls. This script was created to help organize our office's car schedule efficiently.

## Features
- Automatically opens WhatsApp Web
- Searches for a specific WhatsApp group
- Sends two predefined polls
- Simplifies coordination for shared resources

## Requirements
- Python 3.x
- Selenium WebDriver
- Google Chrome
- ChromeDriver (matching your Chrome version)

## Installation (For macOs, Linux)
1. Open your terminal
2. Clone this repository:
   ```sh
   git clone https://github.com/Zakka24/poll-sender.git
   ```
   ```sh
   cd poll-sender
   ```
3. Install dependencies:
   ```sh
   pip install selenium webdriver-manager
   ```
4. Download and install [ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version.
5. Ensure the correct path for the WhatsApp session directory:
   - Modify the script to set the correct path for `user-data-dir` in line 13.
   - You can just comment line 13 and the script will still work correctly, but you have the scan the qr code every time you run the script

## Usage
1. Ensure Google Chrome is installed and ChromeDriver is set up correctly.
2. Run the script:
   ```sh
   python3 script_sondaggio.py
   ```
3. Scan the WhatsApp Web QR code (if required) and let the script send the polls automatically.

## Configuration
- Modify the script to change the target group name.
- Adjust the predefined polls in the script if needed.



