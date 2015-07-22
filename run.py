import redis
from twython import Twython

from config import (redis_url,
                    redis_collection,
                    consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret)


if __name__ == "__main__":

    r = redis.from_url(redis_url)
    
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    tweet = r.spop(redis_collection)

    twitter.update_status(status=tweet)
