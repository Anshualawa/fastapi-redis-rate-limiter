from fastapi import FastAPI, Depends
from app.rate_limiter import rate_limiter


app = FastAPI(title="FastAPI Redis Rate Limiter")


@app.get("/")
def home():
    return {"message":"Welcome to FastAPI Redis Rate Limiter"}

@app.get("/limited", dependencies=[Depends(rate_limiter)])
def limited_endpoint():
    return {"message":"You can access this endpoint"}