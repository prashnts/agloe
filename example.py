import skimage.io

from hello.argleton.model import MapShots

# Load webpage
agloe = MapShots()

# Get your image and Show it
skimage.io.imshow(agloe.traffic)
skimage.io.show()

skimage.io.imshow(agloe.road)
skimage.io.show()

skimage.io.imshow(agloe.map)
skimage.io.show()


