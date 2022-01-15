
# add a hidden message at the end of jpg file using bite code
# ab = apend bites
with open('photo.jpg', 'ab') as file:
    file.write(b"Hello World")
    
    
    
# rb = read bites
with open('photo.jpg', 'rb') as file:
    content = file.read()
    # get index where jpg ends
    offset = content.index(bytes.fromhex('FFD9'))
    file.seek(offset + 2)
    
    #print hidden message
    print(file.read())
