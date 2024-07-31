# Web-Scraping-Ecommerce-Price-Tracker
The Web-Scraping-Ecommerce-Price-Tracker is a Python-based tool designed to monitor the price of the iPhone 15 across multiple e-commerce websites. This project helps users track price changes and make informed budget decisions. It scrapes price data, converts it to Canadian Dollars (CAD), logs it in a CSV file, and sends email notifications based on specific criteria and visualizes the data using PowerBI.

<img src = "https://github.com/Frances-Odunaiya/Web-Scraping-Ecommerce-Price-Tracker/blob/main/Iphone%2015%20price%20Tracker.png" alt = "Price-Tracker" />

## Features
**Web Scraping**: Extracts price data for the iPhone 15 from Flipkart, Amazon, and Cellular Savings using Selenium.
**Currency Conversion**: Converts extracted prices to Canadian Dollars (CAD) for uniformity.
**Data Logging**: Logs the price data into a CSV file for easy access and analysis.
**Email Notifications**: Sends email alerts based on specific price criteria to keep users updated.
**Data Visualization**: Utilizes PowerBI and Tableau to visualize the tracked data, providing insightful charts and graphs.
**Automation**: Uses Microsoft Scheduler to run the scraping scripts at random times automatically.

## Use Cases
- **Price Tracking**: Keep track of price fluctuations for the iPhone 15.
- **Budget Management**: Make informed purchasing decisions based on price trends and historical data.

## Technologies Used
- **Python**: For web scraping, data processing, and automation.
- **Selenium**: For automated browsing and extracting data from web pages.
- **Pandas**: For data manipulation and storage.
- **Smtplib**: For sending email notifications.
- **PowerBI**: For visualizing the data and creating insightful reports.
- **Microsoft Scheduler**: For automating the execution of the scraping scripts.

## How It Works
- **Scraping Data**: The tool scrapes price information for the iPhone 15 from Flipkart, Amazon, and Cellular Savings at random times using an automated script managed by Microsoft Scheduler.
- **Converting Prices**: Extracted prices are converted to CAD.
- **Logging Data**: Price data is logged into a CSV file for record-keeping.
- **Sending Notifications**: Email notifications are sent if prices are retrieved successfully.
- **Visualizing Data**: Data is visualized using PowerBI and Tableau to help users understand price trends and make informed decisions.

## Experiment Results
**Flipkart**: The prices for the iPhone 15 fluctuated throughout the experiment. Initially, Flipkart offered the lowest price, but by the end of the experiment, it had the highest price. This indicates that Flipkart is prone to give discounts and might be the best website to visit when considering buying an iPhone 15.
**Amazon and Cellular Savings**: The prices for the iPhone 15 remained fixed throughout the experiment.

## Installation & Usage
1. Clone the repository:
      ```bash
      Copy code
      git clone https://github.com/yourusername/Web-Scraping-Ecommerce-Price-Tracker.git
   
2. Install required dependencies:
     ```bash
     Copy code
     pip install -r requirements.txt

3. Run the script:
     ```bash
     Copy code
     python price_tracker.py


## Conclusion
The Web-Scraping-Ecommerce-Price-Tracker is a comprehensive tool for anyone looking to monitor the price of the iPhone 15 effectively. Its ability to convert prices to CAD, log data, send notifications, and visualize trends makes it an ideal solution for budget-conscious shoppers and data enthusiasts alike. Based on the experiment results, Flipkart may offer the best deals on the iPhone 15 due to its price fluctuations and discount patterns.
