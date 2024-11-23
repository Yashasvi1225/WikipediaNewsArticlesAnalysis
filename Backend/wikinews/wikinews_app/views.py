from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from .utils.TrendingTopics import read_parquet_files_from_last_hour, get_top_trending_topics

# Create your views here.
output_dir = "C:/Kafka/output/test_output"

def get_trending_topics(request):
    # Step 1: Read the parquet files from the last hour
    data = read_parquet_files_from_last_hour(output_dir)

    # Step 2: Get top 10 trending topics based on precomputed decayed average weight
    top_topics = get_top_trending_topics(data)

    # Convert the top topics to a list of dictionaries
    topics_list = top_topics.select("page_title", "decayed_avg").collect()

    # Prepare the response as a list of dictionaries
    trending_topics = [{"page_title": row['page_title'], "decayed_avg": row['decayed_avg']} for row in topics_list]

    # Return the top 10 topics as a JSON response
    return JsonResponse({"trending_topics": trending_topics}, safe=False)
