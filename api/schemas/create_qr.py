from typing import Optional
from pydantic import BaseModel

class Qr(BaseModel):
    name: str # qr name
    data: str # link
    config: str = "PNG"# png, next features: svg
    color: Optional[str] = "#000000" # hex or black
    bg_color: Optional[str] = "transparent" # hex or transparent
    size: Optional[int] = 10 # 240x240 to 72ppp
