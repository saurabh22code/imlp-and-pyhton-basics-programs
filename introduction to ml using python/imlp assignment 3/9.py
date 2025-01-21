'''
Q.9. What is Web Scrapping?

Web scraping is the process of extracting data from websites by automatically parsing the HTML or XML content of a webpage. This technique is used to gather information from the web for various purposes, such as data analysis, market research, news aggregation, and more.
Key Components of Web Scraping:
1.	Requesting the Web Page:
o	Web scraping typically starts by sending an HTTP request to a specific URL. This request can be made using libraries like requests in Python to retrieve the page's HTML content.
2.	Parsing the HTML:
o	After obtaining the webpage, the HTML content is parsed to extract the desired data.
o	Libraries like BeautifulSoup (from bs4) and lxml are commonly used to parse and navigate the HTML structure.
3.	Extracting Data:
o	The data is extracted by identifying specific HTML tags, classes, or IDs that contain the desired information.
o	You can use CSS selectors or XPath expressions to pinpoint the exact elements.
4.	Storing the Data:
o	Once the relevant data is extracted, it can be stored in various formats like CSV, JSON, or directly into a database for further analysis or use.
Example of Web Scraping in Python:
Here’s a simple example using Python's requests and BeautifulSoup to scrape data from a website:'''
    
import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "https://example.com"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data (for example, all headings)
headings = soup.find_all('h1')

# Step 4: Print the extracted headings
for heading in headings:
    print(heading.text)
