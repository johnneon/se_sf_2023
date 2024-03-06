from fastapi import FastAPI
from routing.translator import router as translator_routing
from constants import MAIN_ROUTE, MAIN_RESPONSE

app = FastAPI()

app.include_router(translator_routing)


@app.get(MAIN_ROUTE)
async def root():
    """Empty method, just for test is app running"""

    return {"message": MAIN_RESPONSE}
