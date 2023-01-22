from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from PIL import Image
from ..schemas.create_qr import Qr
from io import BytesIO
import base64
import qrcode
from ..helpers.to_rgb import to_rgb

qr = APIRouter()

@qr.get("/")
def opening_message():
    message = "Hello, if you can see this message it means that you are using my \
qr generator app correctly. Thank you! :)"
    return message




@qr.post("/create_qr")
async def create_qr(info: Qr):
    url = info.data


    # Crea el QR
    qr = qrcode.QRCode(version=1, box_size=info.size, border=2 )
    qr.add_data(url)
    qr.make(fit=True)
    # print(to_rgb())
    img = qr.make_image(fill_color=to_rgb(info.color), back_color=to_rgb(info.bg_color))
    # img = qr.make_image(fill_color="black", back_color="white")

    # Guarda el QR en un buffer
    buffer = BytesIO()
    img.save(buffer, "PNG")
    # Obtiene los bytes del QR
    qr_bytes = buffer.getvalue()
    # Codifica los bytes en base64
    qr_base64 = base64.b64encode(qr_bytes).decode()
    # Crea un link para descargar el QR
    qr_link = f"data:image/png;base64,{qr_base64}"

    return {"link": qr_link}


