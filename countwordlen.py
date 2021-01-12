from PIL import Image
import os
imgwidth={}

for img in os.listdir('./myfont/'):
	if img.endswith('.png'):
		char,ext=os.path.splitext(img)
		# print(char)
		pic=Image.open("./myfont/"+img)
		imgwidth[char]=pic.width;
