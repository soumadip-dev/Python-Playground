import qrcode

input_url = input("Enter the URL to generate a QR code: ").strip()

output_filename = input(
    "Enter the file name to save the QR code (without extension): "
).strip()

if not output_filename.endswith(".png"):
    output_filename = output_filename + ".png"

qr_image = qrcode.make(input_url)

qr_image.save(output_filename)

print(f"QR code generated successfully and saved as '{output_filename}'.")
