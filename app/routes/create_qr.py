from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from PIL import Image
from ..schemas.create_qr import Qr
# from io import BytesIO
import io
import base64
import qrcode
import json
from ..helpers.converters import to_rgb, to_pts

qr = APIRouter()

# initial greetings 
@qr.get("/")
def opening_message():
    message = "Hi, thanks for using my app! :)"
    return message


# create qr
@qr.post("/create_qr")
async def create_qr(info: Qr):
    url = info.data

    # create qr
    qr = qrcode.QRCode(version=1, box_size=info.size, border=2 )
    qr.add_data(url)
    qr.make(fit=True)

    #  verify whether the background will be transparent or colored
    if (info.bg_color == "transparent"):
        img = qr.make_image(fill_color=to_rgb(info.color), back_color=info.bg_color)
    else:
        img = qr.make_image(fill_color=to_rgb(info.color), back_color=to_rgb(info.bg_color))

    # save qr in buffer
    buffer = io.BytesIO()
    img.save(buffer, info.config)

    # tets the bytes of the qr
    qr_bytes = buffer.getvalue()

    # encodes bytes in base64
    qr_base64 = base64.b64encode(qr_bytes).decode()

    # create a link to download the qr
    qr_link = f"data:image/png;base64,{qr_base64}"

    return {"link": qr_link, "name": info.name}


