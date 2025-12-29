from fastapi import Request, HTTPException
from app.redis_client import redis_client


RATE_LIMIT = 5                  # Requests
TIME_WINDOW = 60        # Seconds


async def rate_limiter(request:Request):
    client_ip  = request.client.host
    key = f"rate_limit:{client_ip}"

    current_requests = redis_client.incr(key)

    if current_requests == 1 :
        redis_client.expire(key, TIME_WINDOW)

    if current_requests > RATE_LIMIT:
        raise HTTPException(
            status_code= 429,
            detail = "too many requests. please try again later."
        )