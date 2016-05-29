import skimage
from skimage import data,io,filters,color


# threshold the image to return boolean pixels
def threshold(image,_type):

	camera = color.rgb2gray(image)
	val = filters.threshold_otsu(camera)
	
	if _type == 'road':
		mask = camera < val
	else:
		mask = camera > val

	return mask


# returns traffic_type corresponding boolean masked image
def traffic_mask(image,traffic_type):

	# take(x,y,3) -- removes alpha channel
	cam = image[:, :, :3]

	if traffic_type=='green':
		mask = cam[:,:,1]!=202
	elif traffic_type=='orange':
		mask = cam[:,:,1]!=125
	elif traffic_type=='red':
		mask = cam[:,:,0]!=230
	elif traffic_type=='maroon':
		mask = cam[:,:,0]!=159
	
	# [0,0,0] for the traffic roads
	cam[mask] = [0,0,0]
	
	# threshold image for the binary image formed
	cam = threshold(cam,'traffic')

	return cam
