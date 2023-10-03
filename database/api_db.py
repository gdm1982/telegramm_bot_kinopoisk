import redis


cache = redis.Redis(host='localhost', port=6379)


def cache_data(key, data, ttl=3600):
    cache.setex(key, ttl, data)


def get_cached_data(key):
    return cache.get(key)
