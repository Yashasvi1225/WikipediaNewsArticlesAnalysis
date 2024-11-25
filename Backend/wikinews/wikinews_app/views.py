from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
import requests
from django.views.decorators.http import require_GET
from .utils.TrendingTopics import read_parquet_files_from_last_hour, get_top_trending_topics
from .News.PageNews import PageNews
from .News.Summarizer import Summarizer
import json

# Create your views here.
output_dir = "C:/Kafka/output/test_output"

def get_trending_topics(request):
    # Step 1: Read the parquet files from the last hour
    data = read_parquet_files_from_last_hour(output_dir)

    # Step 2: Get top 10 trending topics based on precomputed decayed average weight
    top_topics = get_top_trending_topics(data)

    # Convert the top topics to a list of dictionaries
    topics_list = top_topics.select("page_title", "decayed_avg", "avg_view_count").collect()

    # Prepare the response as a list of dictionaries
    trending_topics = [{"page_title": row['page_title'], "decayed_avg": row['decayed_avg'], "view_count": row['avg_view_count']} for row in topics_list]

    # Return the top 10 topics as a JSON response
    return JsonResponse({"trending_topics": trending_topics}, safe=False)


def get_news_articles(request):
    keyword = request.GET.get('keyword', '')  
    summarizer = Summarizer()
     
    try:
        if not keyword:
            return JsonResponse({'error': 'Keyword parameter is required.'}, status=400)
        
        page_news_obj = PageNews(summarizer, keyword)
        json_pages = page_news_obj.fetch_news_article(5)
        json_pages_parsed = json.loads(json_pages)
        # Example: External API request (replace with your actual API URL and key)
        # response = requests.get(
        #     "https://newsapi.org/v2/everything",
        #     params={
        #         'q': keyword,
        #         'apiKey': 'your_news_api_key'  # Replace with your API key
        #     }
        # )

        # if response.status_code == 200:
        #     articles = response.json().get('articles', [])
        #     return JsonResponse({'keyword': keyword, 'articles': articles}, status=200)
        # else:
        #     return JsonResponse(
        #         {'error': 'Failed to fetch news from external API.', 'details': response.text},
        #         status=response.status_code
        #     )

        return JsonResponse({'keyword': keyword, 'articles': json_pages_parsed}, status=200)
    except Exception as e:
        return JsonResponse({'error': 'An error occurred.', 'details': str(e)}, status=500)
