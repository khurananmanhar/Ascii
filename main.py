#/home/runner/Ascii/ayush.jpg
import PIL.Image
import math

toascii = list(reversed(list(" .:-=+*#%@")))

path = input('Please Input Path Location: ')

image = PIL.Image.open(path)
w, h = image.size
if w > h:
	r = h/w
	nw = 200
	nh = int(nw*r)
else:
	r = w/h
	nh = 200
	nw = int(nh*r)
image = image.resize((nw,nh))
image = image.convert('L')
imgVals = PIL.Image.Image.getdata(image)

boxLen = int(255/len(toascii))
imgVals2 = []
for i in imgVals:
	imgVals2.append(toascii[int(i/boxLen) - 1])
imgVals2 = ''.join(imgVals2)

for i in range(0, len(imgVals2), nw):
	print(imgVals2[i:i+nw])
