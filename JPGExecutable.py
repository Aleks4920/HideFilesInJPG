

# embed executable to the end of jpg file
# I used angry IP scanner because it doesnt need any other files to run
with open('photo.jpg', 'ab') as file, open('opscan-win64-3.7.3.exe','rb') as executable:
    file.write(executable.read())
    
    
    
# this will look at the end of the jpg file and create an executable
with open('photo.jpg','rb') as file:
    content = file.read()
    # get index where jpg ends and executable code starts
    offset = content.index(bytes.fromhex('FFD9'))
    
    file.seek(offset + 2)
    # create new executable
    with open('newFile.exe', 'wb') as e:
        e.write(f.read())