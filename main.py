

from page_news import PageNews
from summarization import Summarizer


summarizer = Summarizer()

page_name = "Donald Trump"
page_news_obj = PageNews(summarizer, page_name)

page_news_obj.fetch_news_article(5)



