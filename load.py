import os
import redis

app_name = "GIFTOFTHEARTIST"
redis_collection = 'txt'
redis_url = os.getenv(app_name + '_REDIS_URL', 'redis://localhost:6379')


if __name__ == "__main__":

    r = redis.from_url(redis_url)

    with open('gifts.txt', 'r') as txt:
        for line in txt:
            r.sadd('txt', line.strip())
