from fastapi import APIRouter
from schemas.translator import TranslatorProps
from services.translator import translate as translate_func

router = APIRouter(prefix="/translate")


@router.post("")
async def translate(props: TranslatorProps):
    """Translation method"""

    result = translate_func(props.text)
    return result
