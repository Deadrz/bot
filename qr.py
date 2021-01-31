import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=2,
    )

data = input("Masukan text : ")
sve = input("Masukan nama file : ")
    
#Pengelola Gambar qr
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save(sve+".jpg")
print("File QR di simpan dengan nama "+sve+".jpg")