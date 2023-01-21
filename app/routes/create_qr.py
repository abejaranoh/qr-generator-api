from fastapi import APIRouter
from ..schemas.create_qr import Qr
import qrcode
import io
# from PIL import Image
# import Image

qr = APIRouter()

@qr.get("/")
def opening_message():
    message = "Hello, if you can see this message it means that you are using my \
qr generator app correctly. Thank you! :)"
    return message

@qr.post("/create_qr")
def create_qr(info: Qr):
    url = info.data

    if(info.size == 0):
        info.size = 10

    # create qr object
    qr = qrcode.QRCode(version=1, box_size=info.size, border=2 )

    # add data to qr
    qr.add_data(url)
    qr.make(fit=True)

    # create qr image
    img = qr.make_image(fill_color="black", back_color="white")

    # convert image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    return img_bytes

