import requests
from bs4 import BeautifulSoup

def scrape_discourse(base_url, start_date, end_date):
    # Example: scrape titles (this is minimal, you can expand)
    print(f"Scraping {base_url} from {start_date} to {end_date}")
    resp = requests.get(base_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    titles = [tag.text for tag in soup.find_all('a', class_='title')]
    for title in titles:
        print(title)

if __name__ == "__main__":
    scrape_discourse("https://discourse.onlinedegree.iitm.ac.in/c/tds/50", "2024-01-01", "2024-12-31")
