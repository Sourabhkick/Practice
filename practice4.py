import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = "https://www.ilovepdf.com/pdf_to_word"  # Replace with the actual URL of the webpage

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the <a> tags that contain article titles
    article_links = soup.find_all('a', class_='article-title')  # Replace with the actual HTML structure

    # Loop through the article links and print the titles
    for link in article_links:
        title = link.text.strip()  # Get the text inside the <a> tag
        print(title)
else:
    print("Failed to retrieve the webpage.")

