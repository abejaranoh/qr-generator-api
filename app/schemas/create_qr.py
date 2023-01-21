from typing import Optional
from pydantic import BaseModel

class Qr(BaseModel):
    name: str # qr name
    data: str # url
    config: str # png or svg
    color: Optional[str] # hex color
    bg_color: Optional[str] # hex bg color
    size: Optional[int] # pixels / defaul 240x240 to 72ppp
