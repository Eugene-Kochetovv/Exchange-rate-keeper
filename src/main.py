from fastapi import FastAPI, APIRouter

from currency.router import currency_router


app = FastAPI()


app.include_router(currency_router)

@app.get("/")
async def hello():
    return {"hello": "word"}
