import qrcode as qr
from PIL import Image
r = qr.QRCode(version=1,error_correction=qr.ERROR_CORRECT_H, box_size=20, border=4)
r.add_data("https://www.linkedin.com/in/nouman-irshad-77b9a922b/")
r.make(fit=True)
img = r.make_image(fill_color = "red", back_color = "blue")
img.save("sdddd.png")

# while(True):
#     user = int(input())
#     if (user == 3):
#         print("numi 3")
#     elif(user == 4):
#         print("4")
#     elif (user==6):
#         exit()