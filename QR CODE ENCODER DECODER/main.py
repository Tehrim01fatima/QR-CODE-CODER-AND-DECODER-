# import qrcode

# data = " Hey this my project of qrcode coder and decoder "

# qr= qrcode.QRCode(version= 1, box_size= 10, border=5)

# qr.add_data(data)
# qr.make(fit=True)
# img= qr.make_image(fill_color='red', back_color='white')

# img.save('E:/TEHRIM PROJECTS/python/New folder/QR CODE ENCODER DECODER')
from pyzbar.pyzbar import decode
from PIL import Image

# Open the image
img = Image.open('E:/TEHRIM PROJECTS/python/New folder/QR CODE ENCODER DECODER/my_qrcode.png')

# Decode the QR code
result = decode(img)

# Print the decoded data
for barcode in result:
    print("Type:", barcode.type)
    print("Data:", barcode.data.decode("utf-8"))

