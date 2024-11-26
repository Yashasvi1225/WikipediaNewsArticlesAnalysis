import random
from datasketch import MinHash, MinHashLSH
from sklearn.feature_extraction.text import CountVectorizer

# Sample list of 200 articles
articles = [
    "Article 1 text here...",
    "Article 2 text here...",
    # Add the full content of 200 articles here
    "Article 200 text here..."
]

# Parameters for LSH
shingle_size = 5  # Number of words in each shingle
num_perm = 128  # Number of permutations for MinHash
threshold = 0.5  # Similarity threshold for LSH


# Function to create shingles
def get_shingles(text, shingle_size):
    words = text.split()
    return set([' '.join(words[i:i + shingle_size]) for i in range(len(words) - shingle_size + 1)])


# Initialize MinHashLSH
lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)

# Store original article and its MinHash
minhash_objects = []

# Process each article
for idx, article in enumerate(articles):
    # Create shingles
    shingles = get_shingles(article, shingle_size)

    # Create MinHash
    m = MinHash(num_perm=num_perm)
    for shingle in shingles:
        m.update(shingle.encode('utf8'))

    # Store MinHash object
    minhash_objects.append((article, m))

    # Add to LSH
    lsh.insert(f"article_{idx}", m)

# Retrieve one article from each bucket
buckets = {}
for idx, (article, m) in enumerate(minhash_objects):
    bucket_ids = lsh.query(m)
    if bucket_ids:
        primary_bucket = bucket_ids[0]  # Use the first bucket ID
        if primary_bucket not in buckets:
            buckets[primary_bucket] = article

# Output one representative article from each bucket
print(f"Number of unique buckets: {len(buckets)}\n")
for bucket_id, representative_article in buckets.items():
    print(f"Bucket {bucket_id}: {representative_article[:100]}...")  # Print first 100 characters


