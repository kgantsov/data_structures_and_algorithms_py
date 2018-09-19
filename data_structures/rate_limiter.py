import time
import math


class RateLimiter:
    def __init__(self):
        self.buckets = {}

    def get(self, key):
        pass

    def add(self, key, max_tokens, refill_time, refill_amount):
        bucket = {
            'value': max_tokens,
            'max_tokens': max_tokens,
            'refill_time': refill_time,
            'refill_amount': refill_amount,
            'last_update': time.time(),
        }
        self.buckets[key] = bucket

    def reduce(self, key, tokens=1):
        if key not in self.buckets:
            raise KeyError('Bucket `{}` does not exist'.format(key))

        bucket = self.buckets[key]

        refill_count = math.floor(
            (time.time() - bucket['last_update']) / bucket['refill_time']
        )
        bucket['value'] = min(
            bucket['max_tokens'],
            bucket['value'] + refill_count * bucket['refill_amount']
        )
        bucket['last_update'] = min(
            time.time(), 
            bucket['last_update'] + refill_count * bucket['last_update']
        )

        if tokens > bucket['value']:
            return False

        bucket['value'] -= tokens

        return bucket['value']
