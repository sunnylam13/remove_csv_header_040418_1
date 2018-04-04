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
	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)

	for row in readerObj:
		if readerObj.line_num == 1:
			continue # skip first row
		csvRows.append(row)

	csvFilename.close()
	
	# write out CSV file

