# DDB Library

# Import list
import os

## Current directory
def current_directory():
	return os.path.dirname(os.path.realpath(__file__))

current_dir = current_directory()


## File name splitter
def file_name_splitter(files, splitter):

	try:
		x = files.split(splitter)

		return x

	except:
		print("not working")


## File namer
def namer(first, second, third, fourth, fifth):
	if(third == "none"):
		return first + "_" + second
	elif(fourth == "none"):
		return first + "_" + second + "_" + third
	elif(fifth == "none"):
		return first + "_" + second + "_" + third + "_" + fourth
	else:
		return first + "_" + second + "_" + third + "_" + fourth + "_" + fifth


## CSV folder file checker
def csv_file_checker():

	count = 0

	for file in os.listdir(current_dir):
		csv_file = file_name_splitter(file, ".")

		if (csv_file[1] == "csv"):
			count = count + 1

	if(count == 0):
		print("No CSV file found!")
	elif(count > 1):
		print("Too many CSV files!")
		exit()
	else:
		return file	