import io
#use pillow to convert and read byte arrays of the chosen PNG
import PIL.Image

# img to embed
img = PIL.Image.open('photo.png')

byteArray =  io.BytesIO()
img.save(byteArray, format='PNG')

#  embed a hidden PNG into a JPG
with open('photo.jpg', 'ab') as file:
    file.write(byteArray.getvalue())
    


# extract the hidden PNG by creating new PNG file
with open('photo.jpg','rb') as file:
    content = file.read()
    offset = content.index(bytes.fromhex('FFD9'))
    
    file.seek(offset + 2)
    
    newImage = PIL.Image.open(io.BytesIO(file.read()))
    newImage.save("newPhoto.png")