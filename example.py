import skimage.io
import skimage.draw

from hello.argleton.model import MapShots

# Load webpage
agloe = MapShots()

img = agloe.map

def draw_agent(x, y, img):
	steps = [(100, [100, 20, 255, 50]),
			 (50,  [100, 20, 255, 150]),
			 (20,  [50,  20, 150, 255])]
	for step in steps:
		rr, cc = skimage.draw.circle(x, y, step[0])
		img[rr, cc] = step[1]
	return img


draw_agent(100, 100, img)
draw_agent(100, 120, img)
draw_agent(200, 300, img)

skimage.io.imshow(img)
skimage.io.show()

