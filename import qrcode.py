import qrcode

image = qrcode.make('https://www.facebook.com/chanh.nghia.555542/')
image.save('example_qr.png', 'PNG')