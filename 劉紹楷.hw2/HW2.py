from PIL import Image

im = Image.open('./input.jpg') 
copy = im.copy()
copy.save('./output.jpg')

pixels = im.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        rr, gg, bb = pixels[i, j]
        gray = int((rr + gg + bb)/3)
        pixels[i, j] = ( gray, gray, gray) 
im.save('./grayscale.jpg')
im.show()






