import requests
from bs4 import BeautifulSoup
import json

# Define a list of URLs to scrape data from (you can add more)
urls = [
    'https://en.wikipedia.org/wiki/Web_scraping',
    'https://www.businessinsider.com/guides/tech/how-to-create-a-wikipedia-page',
    'https://en.wikipedia.org/wiki/Artificial_intelligence',
    'https://www.bbc.com/news/technology-67302788',
    'https://www.vocabulary.com/lists/52473'
]

# Create a dictionary to store scraped data
data = []

# Define a function to scrape and store data
def scrape_and_store_data(url, category):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content from the HTML response
        text_content = ""
        for paragraph in soup.find_all('p'):
            text_content += paragraph.get_text() + "\n"

        # Get title, date, and other relevant information
        title = soup.title.string
        date = "your_date_extraction_method_here"

        # Store the data in a dictionary
        page_data = {
            'url': url,
            'title': title,
            'date': date,
            'category': category,
            'text_content': text_content
        }

        data.append(page_data)
        print(f'Scraped data from {url}')

    except requests.exceptions.RequestException as e:
        print(f"Error while scraping {url}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")

# Loop through the list of URLs and scrape data
for url in urls:
    if 'wikipedia.org' in url:
        category = 'Wikipedia'
    elif 'bbc.com' in url:
        category = 'News'
    elif 'businessinsider.com' in url:
        category = 'Blog'
    elif 'vocubulary.com' in url:
        category = 'Words/meanings'
    else:
        category = 'Other'

    scrape_and_store_data(url, category)

# Save the scraped data to a JSON file
with open('scraped_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Data scraping and storage complete.")
