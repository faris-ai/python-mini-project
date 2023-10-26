import qrcode

data = input("Input the data (text/link): ")

img = qrcode.make(data)

path = input("Input the path of directory that you want to save: ")
file_name =input("Input the name of qr code png file: ")

img.save(f'{path}\{file_name}.png')