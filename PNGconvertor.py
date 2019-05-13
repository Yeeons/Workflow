# Converts a 'type'(PNG) with out a Alpha to a JPG
# Removes the original after

# imageconvertor(current_dir, "png") 

## requires PILLOW

import os
from PIL import Image

# image convertor
def imageconvertor(dir, type):
    for files in os.listdir(dir):
		png2jpg_name = files.split(".")

		# converts images
		try:
			if(png2jpg_name[1] == type):
				img_org = Image.open(files)
				rgb_im = img_org.convert('RGB')
				rgb_im.save(png2jpg_name[0] + ".jpg", "JPEG", subsampling=0, quality = 100)

				# removes the png
				os.remove(files)
		except:
			continue
