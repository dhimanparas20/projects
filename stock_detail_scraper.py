import requests
from bs4 import BeautifulSoup
import time
from os import system
# import csv

system("clear")
def fetch_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    all_reviews = []

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    try:
        fetched_dev = soup.find_all('div', class_='factsRow-DS-EntryPoint1-1')

        keys = ["previous_close","avg_volume","market_cap","shares_outstanding","eps","pe","fwd_divident","ex_divident_date"]
        # Dictionary to store the key-value pairs
        result_dict = {}
        result_dict["current_price"] = soup.find('div', class_='mainPrice color_green-DS-EntryPoint1-1').text.strip()

        for i, container in enumerate(fetched_dev):
            # Extract review details and remove any unwanted characters
            value = container.find('div', class_='factsRowValue-DS-EntryPoint1-1').text.strip().replace("\u200e", "")
            
            # Map each cleaned value to a corresponding key
            if i < len(keys):
                result_dict[keys[i]] = value
            else:
                print("Warning: More values than keys provided!")

        return result_dict
    except Exception as e:
        print(f"Exception occurred: {e}")    

    return all_reviews

# Usage
url = "https://www.msn.com/en-gb/money/stockdetails/chef-us-stock/fi-a1plh7?id=a1plh7"
result = fetch_data(url)
print(result)
