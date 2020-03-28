from PIL import Image
def get_black_pic():
    from PIL import ImageGrab
    im = ImageGrab.grab()
    print 'info:', format(im.size)
    # im.save('1.jpg','jpeg')
    # print 'save~'
    # #im.show()
    x = 96
    y = 132
    h = 360
    w = 180
    unit = 18
    small_img = im.crop((x, y, x + w, y + h))
    #small_img.show()
    #small_img.save('black.bmp', 'bmp')
    # raw_input()
    return small_img



#img=get_black_pic()
img=Image.open('black.bmp')
grey_img=img.convert('L')
unit=18
pixel=[[0]*10for i in range(20)]

print '>>>'
for width in range(0,10):
    for height in range(0,20):
        pix=(grey_img.getpixel((9+unit*width,9+unit*height)))
        #print pix
        if pix<50:
            pixel[height][width]='.'
        else:
            pixel[height][width]='0'
for p in pixel:
    for i in p:
        print i,
    print ' '
print pixel
