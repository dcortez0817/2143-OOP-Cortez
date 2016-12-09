import imageEdit
from PIL import Image
import sys


if __name__ == "__main__":
	
	filename = input("jagger.jpg")
	
	try:
		img = Image.open(filename)
	except:
		print("File does not exist")
		sys.exit()
	
	img2 = img.copy()
	img3 = img.copy()
	img4 = img.copy()
	img5 = img.copy()
	img6 = img.copy()
	
	img2.save('copy.jpg')
	
	img = imageEdit.blur(img)
	
	img.save('blur.jpg')
	
	img2 = imageEdit.flip(img2)
	
	img2.save('flip.jpg')
	
	img3 = imageEdit.glass_effect(img3)
	
	img3.save('glass.jpg')
	
	img4 = imageEdit.posterize(img4)
	
	img4.save('poster.jpg')
	
	img5 = imageEdit.warhol(img5)
	
	img5.save('warhol.jpg')
	
	img6 = imageEdit.solarize(img6)
	
	img6.save('solar.jpg')
