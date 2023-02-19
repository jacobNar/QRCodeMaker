import qrcode

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data to the QR code
data = input("Enter the url you want as a QR code: ")
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("my_qr_code.png")
