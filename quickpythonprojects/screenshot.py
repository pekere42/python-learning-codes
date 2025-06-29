import pyscreenshot


#capturing the full screen 
image = pyscreenshot.grab()

#saving image file
desktop_path = r"C:\Users\Enes\Desktop\screenshot.png"
image.save(desktop_path)



#grabbing the part of the screen
#im = pyscreenshot.grab(bbox=(10,10,510,510))#X1,Y1,X2,Y2

#saving the image file
#im.save("screenhot.png")