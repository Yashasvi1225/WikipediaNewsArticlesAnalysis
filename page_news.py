# For every page
# page.fetch_news_article(top_k = 10)
# page.fetch_summary()
import requests
import json
import logging

from content_extractor import ContentExtractor
from summarization import Summarizer


class PageNews:
    """
    Class description.
    """
    page_name = ""
    NEWS_API_KEY = "f049190b6b744976b46acc21a25972f9"
    MARKET_AUX_API_KEY = "TFCpiF4MR8mkme7nrql0RjS8PLsELCUtW6RsUAkD"
    articles = []
    summerizer = None
    page_summary = ""

    def __init__(self, summarizer, page_name):
        self.page_name = page_name
        self.content_extractor = ContentExtractor()
        if summarizer == None:
            return "Could not find a Summerizer"

    def make_newsapi_url(page, date):
        base_url = f"https://newsapi.org/v2/everything?q={page}&from={date}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        return base_url

    def make_currentsapi_url(page):
        base_url = f"https://api.currentsapi.services/v1/search?keywords={page}&language=en"
        return ""
    
    def make_marketaux_url(page):
        base_url = f"https://api.marketaux.com/v1/news/all?symbols=TSLA%2CAMZN%2CMSFT&filter_entities=true&language=en&api_token={MARKET_AUX_API_KEY}"
        return base_url

    
    def fetch_api_responses(api_urls):
        # Configure logging to display messages for debugging
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        responses = {}
        for url in api_urls:
            try:
                logging.info(f"Fetching data from API: {url}")
                response = requests.get(url)
                response.raise_for_status()  # Raises an HTTPError for bad responses
                responses[url] = response.json()
                logging.info(f"Data fetched successfully from {url}")
            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to fetch data from {url}: {e}")
                responses[url] = {"error": str(e)}
        return responses
    
    def fetch_urls(self, data):
        urls = []
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'url' and isinstance(value, str):
                    urls.append(value)
                else:
                    urls.extend(self.fetch_urls(value))
        elif isinstance(data, list):
            for item in data:
                urls.extend(self.fetch_urls(item))
        return urls
    

    def fetch_news_article(self, top_k=100):
        news_api_url = self.make_newsapi_url(self.page_name, '2024-10-14')
        marketaux_api_url = self.make_marketaux_url(self.page_name)
        api_response_objects = self.fetch_api_responses([news_api_url, marketaux_api_url])
        urls = self.fetch_urls(api_response_objects)
        articles = [
            {
                "url": url,
                "title": self.content_extractor.fetch_content(url)[0],
                "content": self.content_extractor.fetch_content(url)[1]
            } 
            for url in urls[:top_k]
        ]
        return json.dumps(articles, indent=2) 
    
    def fetch_article_summary(self, url):
        # Assuming 'articles' is your JSON array of articles
        selected_article = next((article for article in self.articles if article['url'] == url), None)

        if selected_article:
            url = selected_article['url']
            title = selected_article['title']
            content = selected_article['content']
            
            # generate summary
            summary = self.summerizer.generate_summary(f"""{title} \n {content}""")
            return summary
        else:
            return "URL not present in the database. Will have to parse and summarize ad hoc."

    def fetch_page_summary(self):
        if self.page_sumamry != "":
            return self.page_summary
        else:
            # Join all summaries into a single string
            joined_summary = "\n".join(article['summary'] for article in self.articles)
            self.page_summary = self.summerizer.generate_summary(joined_summary)
            return self.page_summary








