import glob
from pathlib import Path
import os
import re

def get_files(directory):
	lst = []
	list_of_files = os.listdir(".")
	for i in list_of_files:
		lst = lst + re.findall(r'img\d+.*', i)
	return lst

def get_file_to_rename(directory):
	lst = []
	list_of_files = os.listdir(".")
	for i in list_of_files:
		lst = lst + re.findall(r'img_\d_\d_\d_lock.*', i)
	return lst

def get_extension(filename):
	return re.findall(r'\.(.+)', filename)

def rename_file(directory):
	lst = []
	for i in get_files(directory):
		lst = lst + re.findall(r'\d+', i)
	lst = [int(i) for i in lst]
	files = get_file_to_rename(directory)
	extensions = [get_extension(i)[-1] for i in files]
	for idx, file in enumerate(files):
		if len(lst) == 0:
			os.rename(file, ('img'+str(0)+'.'+extensions[idx]))
		else:
			os.rename(file, ('img'+str(max(lst)+idx+1)+'.'+extensions[idx]))

if __name__ == '__main__':
	print(f'Found following files: {get_files(os.getcwd())}')
	print(f'File to be renamed is: {get_file_to_rename(os.getcwd())}')
	rename_file(os.getcwd())
