import requests
from bs4 import BeautifulSoup
# Step 1: Send a request to the website
url = "https://www.imdb.com/title/tt2625030/"
response = requests.get(url)
# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
# Step 3: Extract data (for example, all headings)
headings = soup.find_all('h1')
# Step 4: Print the extracted headings
for heading in headings:
 print(heading.text)
