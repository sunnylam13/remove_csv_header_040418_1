# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 remove_csv_header_040418_1.py

import csv,os

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

# create a directory for output
os.makedirs('headerRemoved',exist_ok=True)

# loop through every file in the current working directory
# where '.' is cwd
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue # skip non-csv files

	print('Removing header from ' + csvFilename + ' ...')

	# read the CSV file in (skipping first row)
	
	# write out CSV file

