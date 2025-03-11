# Pool Sender

## Description
Pool Sender is a simple Python script that automates sending polls on WhatsApp Web. It opens WhatsApp Web, navigates to a specified group, and sends two predefined polls. This script was created to help organize our office's car schedule efficiently.

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

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/pool-sender.git
   cd pool-sender
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Download and install [ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version.

## Usage
1. Ensure Google Chrome is installed and ChromeDriver is set up correctly.
2. Run the script:
   ```sh
   python pool_sender.py
   ```
3. Scan the WhatsApp Web QR code (if required) and let the script send the polls automatically.

## Configuration
- Modify the script to change the target group name.
- Adjust the predefined polls in the script if needed.

