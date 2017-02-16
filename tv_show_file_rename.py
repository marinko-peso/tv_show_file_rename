# -*- coding: utf-8 -*-
import sys
import os
import io
import re

# Allowed types of files to be renamed.
ALLOWED_FILE_TYPES = (".srt", ".sub", ".avi", ".mp4")


def rename_file(file_name):
	"""
	Process should happen in the following order:
	- check is this file allowed to be processed
	- check is the file containing 2 numbers
	- use the numbers to rename the file
	"""
	if not allowed_file_type(file_name):
		print "--> %s is not supported. No action taken." % file_name
		return

	# Get the general information about the file being renamed.
	file_location = os.path.dirname(file_name)
	original_file_name_with_ext = os.path.basename(file_name)
	original_file_name = os.path.splitext(original_file_name_with_ext)[0]
	original_file_ext = os.path.splitext(original_file_name_with_ext)[1]

	# Extract numbers from the original file name.
	# We expect two numbers, if less or more we don't do a thing
	file_numbers = re.findall(r'\d+', original_file_name)
	if len(file_numbers) != 2:
		print "--> %s doesn't have 2 numbers in its name. No action taken." % file_name
		return

	# Create the new name for the file and rename it.
	new_file_name = "S%sE%s" % (file_numbers[0], file_numbers[1])
	new_file_full_name = os.path.join(file_location, new_file_name + original_file_ext)
	os.rename(file_name, new_file_full_name)
	print "--> %s successfuly renamed to %s." % (original_file_name, new_file_name)


def process_directory(dir_path):
	"""
	Process should happen in the following order:
	- get the list of files available in the directory
	- if no files are found nothing will happen
	- if some files are detected process them one by one
	"""
	files = os.listdir(dir_path)
	if files:
		print "Directory detected, attempting to process files:"
		for current_file in files:
			file_path = os.path.join(dir_path, current_file)
			if not os.path.isdir(file_path):
				rename_file(file_path)
			else:
				print "--> %s is a directory. No action taken." % file_path
	else:
		"Directory %s is empty. Aborting." % dir_path


def process_directory_sent(dir_path):
	"""
	Check is the parameter sent actually a directory and if so process it.
	"""
	# Or is it a directory?
	if os.path.isdir(dir_path):
		process_directory(dir_path)
	else:
		print "Please specify directory containg files."


def allowed_file_type(file_name):
	"""
	Check file has one of the allowed file extensions.
	Return boolean based on check.
	"""
	return file_name.lower().endswith(ALLOWED_FILE_TYPES)


def main():
	"""
	Check arguments being sent and call the method to rename the files in the directory.
	"""
	arguments_sent = sys.argv
	if len(arguments_sent) > 1:
		dir_path = arguments_sent[1]
		process_directory_sent(dir_path)
	else:
		print "Please specify directory containing files."


# Standard boilerplate to run main method.
if __name__ == "__main__":
	main()
