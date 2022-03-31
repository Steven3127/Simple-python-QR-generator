import pyqrcode as QR

print("Place a link: ")
link = input()
print("Name the QR image:")
name = input()

qrcode_enlace = QR.create(f"{link}")
qrcode_enlace.png(f"{name}.png")
