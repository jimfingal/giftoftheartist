import random
import sys

import redis
from twython import Twython

from config import (redis_url,
                    redis_collection,
                    consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret)


if __name__ == "__main__":

    rand_choice = random.randint(1, 5)
    if rand_choice != 5:
        print("Coin flipped to %s, skipping this time." % rand_choice)
        sys.exit()

    r = redis.from_url(redis_url)
    
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    tweet = r.spop(redis_collection)

    twitter.update_status(status=tweet)
