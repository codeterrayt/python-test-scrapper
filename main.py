import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quotes on the page
quotes = soup.find_all('div', class_='quote')

# Open a CSV file to save the data
with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Quote', 'Author', 'Tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the header

    # Loop through quotes and extract data
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = ', '.join(tag.get_text() for tag in quote.find_all('a', class_='tag'))

        # Write the quote data to the CSV file
        writer.writerow({'Quote': text, 'Author': author, 'Tags': tags})

        # Print the quote to the console
        print(f"Quote: {text}\nAuthor: {author}\nTags: {tags}\n")

print("Quotes have been scraped and saved to quotes.csv")
