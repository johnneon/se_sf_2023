from fastapi import FastAPI
from routing.translator import router as translator_routing

app = FastAPI()

app.include_router(translator_routing)


@app.get("/")
async def root():
    """Empty method, just for test is app running"""

    return {"message": "Hello World"}
