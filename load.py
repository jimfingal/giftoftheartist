import redis

from config import redis_collection, redis_url

if __name__ == "__main__":

    r = redis.from_url(redis_url)

    with open('gifts.txt', 'r') as txt:
        for line in txt:
            r.sadd(redis_collection, line.strip())
