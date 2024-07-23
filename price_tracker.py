#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install selenium


# In[20]:


import csv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Exchange rate from INR to CAD
INR_TO_CAD = 0.016  # 1 INR to CAD

# Function to write data to CSV
def write_to_csv(product_name, website, price, currency):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(r'C:\Users\Jenrola\Desktop\Web_Scraping_on_Websites\price_tracker.csv', 'a', newline='') as csvfile:
        fieldnames = ['Timestamp', 'Product Name', 'Website', 'Price', 'Currency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only once when file is created
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Timestamp': timestamp, 'Product Name': product_name, 'Website': website, 'Price': price, 'Currency': currency})

# Function to send email notification
def send_email(subject, message):
    sender_email = 'odunaiyafrances@gmail.com'
    receiver_email = 'odunaiyafrances@yahoo.com'
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # SMTP details for your email provider
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Update with your SMTP port
    smtp_username = 'odunaiyafrances@gmail.com'
    smtp_password = 'vmlb zmxt iwty wwam'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email notification sent successfully")
    except Exception as e:
        print(f"Failed to send email notification: {str(e)}")


# Define sources and XPaths for the products
sources = [
    {
        'name': 'Flipkart',
        'url': 'https://www.flipkart.com/apple-iphone-15-pink-128-gb/p/itm7579ed94ca647?pid=MOBGTAGPNMZA5PU5&lid=LSTMOBGTAGPNMZA5PU51YWTGZ&marketplace=FLIPKART&q=Apple+iPhone+15+%28128+GB%29+-+Pink&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=2431541c-4639-41c8-8aa3-93b0ddf36a69.MOBGTAGPNMZA5PU5.SEARCH&ppt=pp&ppn=pp&ssid=tdo4fvvzbk0000001721153542062&qH=d6ce06b408c0eedc',
        'price_xpath': '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]',
        'product_name_xpath': '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span'
    },
    {
        'name': 'Amazon',
        'url': 'https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX3TW6X/ref=sr_1_7?dib=eyJ2IjoiMSJ9.p2BlrVFqcFx-oYyMC1dOpVcJtHcqJv1JVvf-8ZgrD0bNR5sETLTYyHxWs_aOCHSEQ1Bm17emXd2MYFBTs9LHrv6mfP3FYRHdL6Ztd54y5gcqKg25eKExWtzmSdMZAQVxdBvATHgi_3ggofeJ2gE0W8wRnU4_1-jlSTOT3L0IARjqHcUHkmcOyYkp2q04pwYNZhJ_7e8oaz236nropgXtBSYD2wxrdAAaZIHAOmhh1IfHLgxL3IvbOJPM4QFz5w0SIW1CKXf-dvO1iHIe-yIZLTSX9c_IH7uoLWwzgoRXgv4.HBVDR2W3NHC4lS-nZJwa2rTaD-Ep9XaLya5qC8BDiNk&dib_tag=se&keywords=Apple+iPhone+XS+%28Space+Grey%2C+64+GB%29&qid=1721153496&s=electronics&sr=1-7',
        'price_xpath': '/html/body/div[4]/div/div[3]/div[11]/div[17]/div/div/div[4]/div[1]/span[3]/span[2]/span[2]',
        'product_name_xpath': '/html/body/div[4]/div/div[3]/div[11]/div[3]/div/h1/span'
    },
    {
        'name': 'CellularSavings',
        'url': 'https://cellularsavings.ca/products/iphone-15?variant=49325700546876&currency=CAD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_campaign=gs-2019-03-26&utm_source=google&utm_medium=smart_campaign&gad_source=1&gclid=CjwKCAjwtNi0BhA1EiwAWZaANEhRBEV9jzDjdm7OGZcvR7eUerVZHulEGyNZBuBWo3akBhINfRujehoCz3oQAvD_BwE',
        'price_xpath': '/html/body/div[2]/main/div/div/div[1]/div[2]/div/div[1]/ul/li[2]/span',
        'product_name_xpath': '/html/body/div[2]/main/div/div/div[1]/div[2]/div/div[1]/h1'
    }
]

# Configure Selenium WebDriver
CO = Options()
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
CO.add_argument("--headless")  # Optional: run Chrome in headless mode
CO.add_argument("--disable-gpu")
# Initialize the WebDriver
wd = webdriver.Chrome(options=CO)

try:
    prices = {}

    for source in sources:
        print(f"Connecting to {source['name']}")

        wd.get(source['url'])
        time.sleep(2)  # Adjust as needed or use WebDriverWait for more precision

        product_name_element = wd.find_element(By.XPATH, source['product_name_xpath'])
        price_element = wd.find_element(By.XPATH, source['price_xpath'])

        product_name = product_name_element.text.strip()
        price_text = price_element.text.strip().replace('₹', '').replace(',', '').replace('$', '')

        try:
            price = float(price_text)
        except ValueError:
            print(f"Error converting price '{price_text}' to float on {source['name']}")
            price = None

        if price is not None:
            if source['name'] == 'CellularSavings':
                price_in_cad = price
            else:
                price_in_cad = price * INR_TO_CAD
            
            prices[source['name']] = {'product_name': product_name, 'price': price_in_cad}
            print(f"Product: {product_name}")
            print(f"Price: ${price_in_cad:.2f} CAD")
            print(f" ---> Successfully retrieved the price from {source['name']}\n")
            
            # Write to CSV
            write_to_csv(product_name, source['name'], price_in_cad, 'CAD')
        else:
            print(f"Failed to retrieve price from {source['name']}\n")

    # Final display
    print("#------------------------------------------------------------------------#")
    print(f"Price for [{product_name}] on all websites, Prices are in CAD \n")
    if 'Flipkart' in prices:
        print(f"Price available at Flipkart is: ${prices['Flipkart']['price']:.2f} CAD")
    if 'Amazon' in prices:
        print(f"Price available at Amazon is: ${prices['Amazon']['price']:.2f} CAD")
    if 'CellularSavings' in prices:
        print(f"Price available at CellularSavings is: ${prices['CellularSavings']['price']:.2f} CAD")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    wd.quit()



# In[21]:


timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
message = "Hello there! I have successfully retrieved the prices from all websites today " + timestamp
subject = "WEB SCRAPING COMPLETED ON " + timestamp
send_email(subject, message)


# In[ ]:




