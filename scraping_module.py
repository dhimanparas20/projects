from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional, Union
from urllib.parse import urlparse, parse_qs
import os
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from playwright.sync_api import sync_playwright
import random
import time
import requests
import base64
os.system("clear")

BASE_DOWNLOAD_FOLDER = "downloads"
os.makedirs(BASE_DOWNLOAD_FOLDER, exist_ok=True)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
]

HEADERS = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

def is_scrapable(url):
    """
    Checks if the given URL is scrapable by analyzing the response for CAPTCHA, IP block, or human verification.
    """
    session = HTMLSession()
    try:
        response = session.get(url, headers=HEADERS, timeout=10)
        response.html.render(timeout=20)  # Render JavaScript if necessary
        
        # Check for CAPTCHA indicators
        if "captcha" in response.text.lower() or "human verification" in response.text.lower():
            print(f"{url} is not scrapable due to CAPTCHA or human verification.")
            return False

        # Check for Cloudflare security
        if "Cloudflare" in response.text:
            print(f"{url} has Cloudflare security.")
            return False

        # Check for IP blocking (look for common error messages)
        if response.status_code == 403 or "access denied" in response.text.lower():
            print(f"{url} is not scrapable due to IP blocking.")
            print(f"Response code: {response.status_code}")
            return False
        print(f"{url} is scrapable.")
        return True

    except Exception as e:
        print(f"Error checking scrapability for {url}: {e}")
        return False

def scrape_with_playwright(url):
    """Fetch page content using Playwright to bypass IP blocking or JavaScript rendering."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        content = page.content()
        browser.close()
        return content

class SeleniumScraper:
    def __init__(self, driver_path='./modules/chromedriver'):
        """
        Initializes the Selenium WebDriver with predefined options.
        """
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument(
            f"user-agent={random.choice(USER_AGENTS)}"
        )
        self.chrome_options.add_argument("--window-size=1920x1080")  # Set window size to avoid rendering issues
        self.chrome_options.add_argument("--start-maximized")
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def scrape(self, url,sleep=0):
        """
        Scrapes the given URL using the initialized WebDriver.

        :param url: URL to scrape
        :return: BeautifulSoup object containing the page source
        """
        try:
            print(f"Navigating to {url}...")
            self.driver.get(url)

            # Wait for the page to load completely
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            time.sleep(sleep)  # Additional delay to ensure all content loads

            # Print the redirected URL to confirm success
            print(f"Redirected URL: {self.driver.current_url}")

            # Extract the page source after redirection
            page_source = self.driver.page_source
            print("Page successfully loaded after redirection.")

            # Parse the page source with BeautifulSoup
            soup = BeautifulSoup(page_source, "html.parser")
            print("Soup object successfully created.")
            return soup

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def download_pdf(self, url, output_folder,sleep_time=0):
        """
        Uses Selenium to handle redirections and download a PDF file, including handling `data:` URLs.

        :param url: URL of the PDF or page to download from
        :param output_folder: Folder to save the downloaded PDF
        """
        try:
            # Set up download preferences
            prefs = {
                "download.default_directory": os.path.abspath(output_folder),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True,
            }
            self.chrome_options.add_experimental_option("prefs", prefs)

            print(f"Navigating to {url}...")
            self.driver.get(url)
            print("Navigation Done")

            # Wait for the page to fully load
            time.sleep(sleep_time)  # Adjust this based on the expected load time

            # Get the final URL after redirection
            current_url = self.driver.current_url

            if current_url.startswith("data:"):
                # Handle `data:` URLs (base64-encoded content)
                print(f"Detected direct download via data URL.")
                file_name = url.split("/")[-1].split("?")[0]
                if not file_name.endswith(".pdf"):
                    file_name = f"{file_name}.pdf"

                file_path = os.path.join(output_folder, file_name)

                # Parse the data URL and extract content
                metadata, content = current_url.split(",", 1)
                if "base64" in metadata:
                    content = base64.b64decode(content)
                else:
                    content = content.encode("utf-8")

                # Validate and save the content
                if content.strip():
                    with open(file_path, "wb") as pdf_file:
                        pdf_file.write(content)
                    print(f"Downloaded directly to: {file_path}")
                    return True
                else:
                    print(f"Content is empty. Download failed.")
                    return False

            elif current_url.lower().endswith(".pdf"):
                # Handle direct PDF links
                print(f"Detected direct PDF URL: {current_url}")
                file_name = current_url.split("/")[-1].split("?")[0]
                file_path = os.path.join(output_folder, file_name)

                # Download the file using requests
                response = requests.get(current_url, stream=True,headers=HEADERS)
                if response.status_code == 200 and response.content.strip():
                    with open(file_path, "wb") as pdf_file:
                        for chunk in response.iter_content(chunk_size=1024):
                            pdf_file.write(chunk)
                    print(f"Downloaded: {file_path}")
                    return True
                else:
                    print(f"Failed to download the file. Status Code: {response.status_code}, Content Size: {len(response.content)}")
                    return False

            else:
                # Handle other cases (redirection or non-standard URLs)
                print(f"Final URL: {current_url}")
                response = requests.get(current_url, stream=True,headers=HEADERS)
                if response.status_code == 200 and response.content.strip():
                    print("response code 200")
                    file_name = current_url.split("/")[-1].split("?")[0]
                    print("filename:"+file_name)
                    if not file_name.endswith(".pdf"):
                        file_name = f"{file_name}.pdf"

                    file_path = os.path.join(output_folder, file_name)
                    with open(file_path, "wb") as pdf_file:
                        for chunk in response.iter_content(chunk_size=1024):
                            pdf_file.write(chunk)
                    print(f"Downloaded: {file_path}")
                    return True
                else:
                    print(f"Failed to download the file. Status Code: {response.status_code}, Content Size: {len(response.content)}")
                    return False

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def download_pdf_from_epdf(self,url,output_folder,sleep_time=0):
        try:
            # Open the URL
            self.driver.get(url)
            time.sleep(sleep_time)  # Short wait to ensure content is fully loaded

            # Get the page source and parse it with BeautifulSoup
            soup = BeautifulSoup(self.driver.page_source, "html.parser")

            # Find the iframe containing the PDF URL
            iframe = soup.find("iframe", src=True)
            if iframe:
                pdf_url = iframe["src"]
                print(f"Found PDF URL: {pdf_url}")
                # Extract the arnumber from the URL
                parsed_url = urlparse(pdf_url)
                query_params = parse_qs(parsed_url.query)
                arnumber = query_params.get("arnumber", ["unknown"])[0]  # Default to "unknown" if not found

                # Define the filename based on arnumber
                filename = f"{arnumber}.pdf"
                if filename == "unknown.pdf":
                    print("No File Access")
                    return False
                print(f"Saving as: {filename}")

                # Get cookies from Selenium
                cookies = self.driver.get_cookies()
                session = requests.Session()

                # Set cookies in the requests session
                for cookie in cookies:
                    session.cookies.set(cookie['name'], cookie['value'])

                # Add headers to mimic a browser
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Referer": url,
                }

                # Download the PDF using the session
                pdf_response = session.get(pdf_url, headers=headers)
                if pdf_response.status_code == 200:
                    # Ensure the output directory exists
                    os.makedirs(output_folder, exist_ok=True)
                    output_file = os.path.join(output_folder, filename)
                    with open(output_file, "wb") as file:
                        file.write(pdf_response.content)
                    print(f"PDF downloaded successfully: {output_file}")
                    return True
                else:
                    print(f"Failed to download the PDF. HTTP Status Code: {pdf_response.status_code}")
                    return False
            else:
                print("No iframe containing the PDF URL was found on the page.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False


    def quit_driver(self):
        """
        Quits the WebDriver instance.
        """
        if self.driver:
            self.driver.quit()
            print("WebDriver successfully quit.")

class RequestsHTMLScraper:
    def __init__(self, user_agent: str = random.choice(USER_AGENTS), timeout: int = 30):
        """
        Initialize RequestsHTML Scraper with configurable options
        
        Args:
            user_agent (str, optional): Custom user agent string
            timeout (int): Request timeout in seconds
        """
        
        # Create HTMLSession
        self.session = HTMLSession()
        
        # Configure default headers
        self.session.headers.update(HEADERS)
        
        # Default timeout
        self.timeout = timeout
        
    def scrape(self, url: str, method: str = 'get', params: dict = None, 
               data: dict = None, headers: dict = HEADERS, render: bool = False, 
               wait: int = 20) -> Optional[BeautifulSoup]:
        """
        Scrape a webpage and return BeautifulSoup object
        
        Args:
            url (str): URL to scrape
            method (str): HTTP method (get/post)
            params (dict, optional): URL parameters
            data (dict, optional): POST data
            headers (dict, optional): Additional headers
            render (bool): Whether to render JavaScript
            wait (int): Wait time for rendering in seconds
        
        Returns:
            BeautifulSoup object or None
        """
        try:
            # Prepare headers (merge with default)
            request_headers = self.session.headers.copy()
            if headers:
                request_headers.update(headers)
            
            # Select appropriate method
            if method.lower() == 'get':
                response = self.session.get(
                    url, 
                    params=params, 
                    headers=request_headers,
                    timeout=self.timeout
                )
            elif method.lower() == 'post':
                response = self.session.post(
                    url, 
                    params=params, 
                    data=data, 
                    headers=request_headers,
                    timeout=self.timeout
                )
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            # Render JavaScript if requested
            if render:
                response.html.render(timeout=wait)
            
            # Raise an exception for bad status codes
            response.raise_for_status()
            
            # Create BeautifulSoup object
            soup = BeautifulSoup(response.html.html, 'html.parser')
            
            print(f"Successfully scraped: {url}")
            return soup
        
        except requests.RequestException as e:
            print(f"Error scraping {e}")
            return None
        except Exception as e:
            print(f"Unexpected error scraping {url}: {e}")
            return None

    def download_pdf(self, url: str, download_folder, custom_filename: str = None, render: bool = False, 
                    wait: int = 5) -> Optional[str]:
        """
        Download PDF from a given URL with multiple handling strategies
        
        Args:
            url (str): URL to download PDF from
            custom_filename (str, optional): Custom filename for the downloaded PDF
            render (bool): Whether to render JavaScript before downloading
            wait (int): Wait time for rendering
        
        Returns:
            str: Path to downloaded PDF file or None
        """
        self.download_folder = download_folder
        try:
            # Send initial request
            response = self.session.get(
                url, 
                timeout=self.timeout
            )
            
            # Render JavaScript if requested
            if render:
                response.html.render(timeout=wait)
            
            # Raise an exception for bad status codes
            response.raise_for_status()
            
            # Determine filename
            if custom_filename:
                filename = custom_filename if custom_filename.endswith('.pdf') else f"{custom_filename}.pdf"
            else:
                # Try to extract filename from URL or response headers
                filename = self._extract_filename(url, response)
            
            # Full file path
            file_path = os.path.join(self.download_folder, filename)
            
            # Handle different content types
            content = response.content
            
            # Check for data URL
            if isinstance(response.url, str) and response.url.startswith('data:'):
                # Handle base64 encoded data URLs
                metadata, content_str = response.url.split(',', 1)
                if 'base64' in metadata:
                    content = base64.b64decode(content_str)
            
            # Validate and save the content
            if content and len(content) > 0:
                with open(file_path, 'wb') as pdf_file:
                    pdf_file.write(content)
                
                print(f"Successfully downloaded PDF: {file_path}")
                return file_path
            
            # Fallback download method
            return self._fallback_download(url, filename)
        
        except Exception as e:
            print(f"Error downloading PDF from {url}: {e}")
            # Attempt fallback download method
            return self._fallback_download(url, custom_filename)
    
    def _extract_filename(self, url: str, response) -> str:
        """
        Extract filename from URL or response headers
        
        Args:
            url (str): Original URL
            response: Response object
        
        Returns:
            str: Extracted filename
        """
        # Check Content-Disposition header
        content_disposition = response.headers.get('Content-Disposition')
        if content_disposition:
            import re
            filename_match = re.search('filename=(.+)', content_disposition)
            if filename_match:
                return filename_match.group(1).strip('"\'')
        
        # Extract from URL
        filename = url.split('/')[-1].split('?')[0]
        
        # Ensure .pdf extension
        if not filename.lower().endswith('.pdf'):
            filename = f"{filename}.pdf"
        
        return filename
    
    def _fallback_download(self, url: str, filename: str = None) -> Optional[str]:
        """
        Fallback download method using requests
        
        Args:
            url (str): URL to download from
            filename (str, optional): Custom filename
        
        Returns:
            str: Path to downloaded file or None
        """
        try:
            # Determine filename if not provided
            if not filename:
                filename = url.split('/')[-1].split('?')[0]
                if not filename.lower().endswith('.pdf'):
                    filename = f"{filename}.pdf"
            
            # Full file path
            file_path = os.path.join(self.download_folder, filename)
            
            # Download using requests
            with requests.get(url, stream=True, timeout=self.timeout,headers=HEADERS) as r:
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            
            print(f"Fallback download successful: {file_path}")
            return file_path
        
        except Exception as e:
            print(f"Fallback download failed for {url}: {e}")
            return None    

    def close_session(self):
        """
        Cleanup method to close the session
        """
        if hasattr(self, 'session'):
            self.session.close()

seleniumScraper = SeleniumScraper()
requestsHtmlScraper = RequestsHTMLScraper()
print("-----------------|STARTING THE SHIT|-----------------------------")
print()
