from PIL import Image

im = Image.open('pig.jpg').convert('L')
pixels = im.getdata()          # get the pixels as a flattened sequence
black_thresh = 50
nblack = 0
for pixel in pixels:
    if pixel < black_thresh:
        nblack += 1
n = len(pixels)

if (nblack / float(n)) > 0.5:
    print("mostly black")