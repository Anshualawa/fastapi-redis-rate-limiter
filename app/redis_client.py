from redis import Redis

redis_client = Redis(
    host="127.0.0.1",
    port=6379,
    decode_responses=True
)