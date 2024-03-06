from fastapi import APIRouter
from schemas.translator import TranslatorProps
from services.translator import translate as translate_func
from constants import TRANSLATE_ROUTE, TRANSLATE_ROUTE_POST

router = APIRouter(prefix=TRANSLATE_ROUTE)

@router.post(TRANSLATE_ROUTE_POST)
async def translate(props: TranslatorProps):
    """Translation method"""

    result = translate_func(props.text)
    return result
