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
        fetched_dev = soup.find('div', class_='zr_rankbox composite_group')
        head_data = fetched_dev.find("p",class_="rank_view")
        main_data = head_data.find_all("span",class_="composite_val")

        keys = ["value","growth","momentum","vgm"]
        # Dictionary to store the key-value pairs
        result_dict = {}
        result_dict['insdustry'] = soup.find("a",class_="sector").text.replace("Industry:","").strip()

        for i, container in enumerate(main_data):
            # Extract review details and remove any unwanted characters
            value = container.text.strip()
            
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
url = "https://www.zacks.com/stock/quote/ZIM"
result = fetch_data(url)
print(result)
