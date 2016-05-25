import skimage
import os
from skimage import color
from skimage import data,io,filters

def read_image(image_path):
	#filename = os.path.join(skimage.data_dir, '/home/parul/Downloads/bmap.png')
	filename = os.path.join(skimage.data_dir, image_path)
	camera = io.imread(filename)

	#io.imshow(camera)
	#io.show()

	return camera

def threshold(image,_type='roads'):

	camera = color.rgb2gray(image)
	val = filters.threshold_otsu(camera)
	
	if _type == 'roads':
		mask = camera < val
	else:
		mask = camera > val

	return mask

def coordinates(image_path,_type='roads'):

	image = read_image(image_path)

	if _type == 'roads':
		masked_image = threshold(image,_type)
	elif _type == 'traffic_g':
		masked_image = green_mask(image)
	elif _type == 'traffic_o':
		masked_image = orange_mask(image)
	elif _type == 'traffic_r':
		masked_image = red_mask(image)
	elif _type == 'traffic_m':
		masked_image = maroon_mask(image)

	q=[]
	for i in range(len(masked_image)):
		k=[]
		for j in range(len(masked_image[i])):
			if masked_image[i][j]==True:
				k.append((i,j))
		q.append(k)

	return q

def green_mask(image):

	cam = image[:, :, :3]
	green = cam[:,:,1]!=202
	cam[green] = [0,0,0]
	cam = threshold(cam,'traffic')

	return cam

def orange_mask(image):

	cam = image[:, :, :3]
	orange = cam[:,:,1]!=125
	cam[orange] = [0,0,0]
	cam = threshold(cam,'traffic')

	return cam


def red_mask(image):

	cam = image[:, :, :3]
	to_delete = cam[:,:,1]>1
	to_delete1 = cam[:,:,2]>1
	cam[to_delete] = [0,0,0]
	cam[to_delete1] = [0,0,0]

	cam = threshold(cam,'traffic')

	return cam

def maroon_mask(image):

	cam = image[:, :, :3]
	maroon = cam[:,:,0]!=159
	cam[maroon] = [0,0,0]
	cam = threshold(cam,'traffic')

	return cam



if __name__ == '__main__':
	
	image_path = '/home/parul/Downloads/tmap.png'
	_type = 'traffic_g'
	co_ordlist = coordinates(image_path,_type)