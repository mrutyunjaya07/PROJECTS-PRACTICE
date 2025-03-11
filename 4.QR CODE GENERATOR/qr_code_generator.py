# 

import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename (e.g., qr_code.png): ").strip()

# Ensure the filename has a valid image extension
if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
    filename += ".png"  # Default to PNG

try:
    qr = qrcode.QRCode(box_size=20, border=8)
    qr.add_data(data)
    qr.make(fit=True)  # Ensure the QR code resizes properly
    image = qr.make_image(fill_color="red", back_color="white")
    
    image.save(filename)
    print(f"QR code saved as {filename}")
except Exception as e:
    print(f"Error generating QR code: {e}")
