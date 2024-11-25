from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unix_timestamp,to_timestamp
from datetime import datetime, timedelta
import pytz

# Path to the directory where the Parquet files are stored
output_dir = "C:/Kafka/output/test_output"

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Trending Topics Analysis") \
    .getOrCreate()

# Function to read Parquet files from the last one hour
def read_parquet_files_from_last_hour(output_dir):
    try:
        # Get the current time and time 1 hour ago
        now = datetime.now()
        one_hour_ago = now - timedelta(hours=1)

        # Read all Parquet files in the directory
        data = spark.read.parquet(output_dir)

        # Ensure the 'window' column is in timestamp format
        data = data.withColumn("window", to_timestamp(col("window.start")))  # Adjust column name if needed

        # Filter the data to only include records from the last hour
        filtered_data = data.filter(col("window") >= one_hour_ago.strftime('%Y-%m-%d %H:%M:%S'))
        return data

    except Exception as e:
        print(f"Error reading parquet files: {e}")
        return None

# Function to get the top 10 trending topics based on the existing weights
def get_top_trending_topics(data):
    try:
        # Sort by the 'decayed_avg' (or 'total_weight') in descending order and get the top 10 topics
        top_topics = data.orderBy(col("decayed_avg").desc()).limit(10)
        return top_topics
    except Exception as e:
        print(f"Error processing trending topics: {e}")
        return None