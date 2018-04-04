# Remove Header from CSV Files

This program removes the first line from CSV files, often the header row.  It opens every file with the `.csv` extension in the current working directory, reads in the contents and rewrites the contents without the first row...  all to a file of the same name.  This replaces the old contents of the CSV file with the new, headless content.

## Test Data

	/test/removeCsvHeader.zip

unzip this to the current working directory

	/remove_csv_header

now you have test files for program

alternatively you can alter the program to access the directory without copying after unzipping in `/test`

	./tests/removeCsvHeader.zip%20Folder

## Resources

ABSP:  543

