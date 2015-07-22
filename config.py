import os

app_name = "GOTA"
redis_collection = 'txt'

consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')

redis_url = os.getenv(app_name + '_REDIS_URL', 'redis://localhost:6379')
