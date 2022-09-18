from Combined. StegaPy.stegapy import create_image


def enimage(message, imgname, Dfilename):
    message = message   # Rush is a seperator while decrypting
    create_image(message, imgname, Dfilename)

# encode("Hello")
