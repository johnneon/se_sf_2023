from pydantic import BaseModel

class TranslatorProps(BaseModel):
    text: str
