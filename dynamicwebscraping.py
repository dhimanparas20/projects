from requests_html import HTMLSession
from os import system

system("clear")

# Create an HTML session
s = HTMLSession()

# Specify the URL of the webpage you want to scrape
query = "shimla"
url = f"https://www.google.com/search?q={query}+weather"
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
data = 0 
# Send a GET request and render the JavaScript content
while True:
    r = s.get(url, headers={'User-Agent': user_agent})
    old = data 
    try:
        data = r.html.find("span#wob_tm.wob_t.q8U8x",first=True).text
        # data = r.html.find("table",first=True).text
    except:
        data = old   
    if old!= data :
        old = data
        print("========================")
        print(data)
        print("========================")
    #data = r.html.find("table",first=True).text
print("exit")    
