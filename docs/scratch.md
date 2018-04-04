# Scratch Notes and Log

## Wednesday, April 4, 2018 9:36 AM

NOTE:  whenever you write a program that alters files, be sure to back up the files just in case program screws up...  as you don't want to erase your originals...

program actions

* find all CSV files in current working directory

* read the full contents of each

* write out contents, skipping first line, to new CSV

code level

* loop over list of files from `os.listdir()`, skipping non-CSV

* create CSV `Reader` object and read in contents, using `line_num` attribute to figure out which line to skip

* create CSV `Writer` object and write out the read data to new file

