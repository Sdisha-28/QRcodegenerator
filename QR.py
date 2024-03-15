import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,box_size=5,border=2,error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("www.google.com")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("GOOGLE.png")