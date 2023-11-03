import requests
from bs4 import BeautifulSoup
import sqlite3

# Send an HTTP GET request to the website
url = 'http://quotes.toscrape.com'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the website (quotes in this case)
    quotes = soup.find_all('span', class_='text')

    # Create a SQLite database and a table
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS quotes (quote TEXT)')

    # Insert scraped quotes into the database
    for quote in quotes:
        c.execute('INSERT INTO quotes VALUES (?)', (quote.get_text(),))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    print('Scraped data saved to the database.')

else:
    print('Failed to retrieve the page. Status code:', response.status_code)