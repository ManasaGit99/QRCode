import qrcode as qr
#import image
qrc=qr.QRCode(
    version= 15, #high the number bigger the QRCODE image
    box_size= 10, #size of the box ( number of pixles for each box in QRCODE )
    border=5    #border in all 4 sides (White color)


)
data = "https://en.wikipedia.org/wiki/MS_Dhoni"

# we can use link or Text
# Text should be written in quotes
# example data1="HELLO WORLD!"

qrc.add_data(data)
qrc.make(fit=True)
img = qrc.make_image(file="black" , back_color  =  "white")
img.save("test.png")