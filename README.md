# FastAPI Redis Rate Limiter 🚀

A simple API rate limiter built using FastAPI and Redis.

## Features
- IP based rate limiting
- Redis atomic counters
- Automatic key expiry
- Middleware-like dependency

## Tech Stack
- FastAPI
- Redis
- Python

## How it works
- Each client IP is stored as a Redis key
- Redis INCR tracks request count
- EXPIRE resets counter after time window
- Exceeds limit → HTTP 429

## Run Locally
1. Start Redis server
2. Install dependencies
3. Run FastAPI server

## Example
Max 5 requests per minute per IP
