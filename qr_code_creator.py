import pyqrcode

url = input("Enter the URL to generate QR code: ")

qr = pyqrcode.create(url)
qr.svg("qr.svg", scale=6)