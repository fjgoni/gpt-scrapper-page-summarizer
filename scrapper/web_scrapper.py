import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"

        content_div = soup.find('div', class_='available-content')
        if content_div:
            for tag in content_div(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = content_div.get_text(separator="\n", strip=True)
        else:
            self.text = "No 'available-content' section found"

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\n\nAvailable Content:\n{self.text}"
    
    def scrape_full_page_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text  # HTML como string
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

