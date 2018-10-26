## TODO
# Set was created early in the coding, as I went further it's probable not required and could be replaced with a list
# Find a CSV file to check against Return errors for 0 or more then 1 CSV file in folder.

import os
from DDB_Library import current_directory, file_name_splitter, namer, csv_file_checker

current_dir = current_directory()


with open(csv_file_checker(), "r") as ins:
    array = []
    for line in ins:
        array.append(line)

count = 0
count2 = 0
none = "none"

missing_array = set()
checker_array = []


# looks through CSV file
while len(array) > count:

	master = array[count].split("\t")
	docSizeFinal = master[2].rstrip()
	publisher = master[0]
	state = master[1]

	# looks through directory
	for file in os.listdir(current_dir):
		
		imagefile = file_name_splitter(file, ".")

		if (imagefile[1] == "jpg"):

			creative_file = file_name_splitter(imagefile[0], "_")
			creative_publisher = creative_file[1]
			creative_state = creative_file[2]
			creative_size = creative_file[3]

			checker_array.append(namer(creative_publisher, creative_state, creative_size, none, none))

			# checks CSV vs diretory
			if(creative_publisher == publisher and creative_state == state and creative_size == docSizeFinal):
				print("match found!: " + file)
				os.rename(file, imagefile[0] + "_M." + imagefile[1])

			else:
				missing_array.add(namer(publisher, state, docSizeFinal, none, none))

	count = count + 1


# checks for missing files
for x in missing_array:
    if x not in checker_array:
    	print("Missing size: " + x)