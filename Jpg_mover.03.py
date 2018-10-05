# Will need renaming logic when we go to roll out the campaign

import os
from glob import glob
from PNGconvertor import imageconvertor


# curent directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# wildcard subfolders
folder = glob(current_dir + "/*/*/")

for dir in folder:
	for file in os.listdir(dir):

		img_name = file.split(".")
		img_path = os.path.join(dir, file)

		listdir = []

		try:
			# if the file is a jpg
			if(img_name[1] == "png"):

				new_destination = img_path.split("/")
				new_destination_total = len(new_destination)

				i = 0

				# moves the file up 2 directory (the number 3 is for campagin/lvl2/lvl1/)
				while new_destination_total-3 > i:
					listdir.append(new_destination[i])
					i = i + 1

				tots = len(listdir)
				# (the number 1 is for campagin/lvl2/lvl1/)
				info = listdir[tots-1]

				new_path = "/".join(listdir)

				# img_new_path = new_path + "/" + file
				img_new_path = new_path + "/" + info + "_" + img_name[0] + "." + img_name[1]

				# moves the image
				os.rename(img_path, img_new_path)
		except:
			continue

imageconvertor(current_dir, "png")