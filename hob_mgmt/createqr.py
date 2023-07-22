import qrcode
import os

def createQR(pg_no):
    # QRコード生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(pg_no)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f'hob_mgmt/static/QRcode/{pg_no}.png')

#  createQR(pg_no)