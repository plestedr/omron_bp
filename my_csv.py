import csv 
import argparse

# csv file name 
# filename = "BloodPressure_11-Sep-2019.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

parser = argparse.ArgumentParser(description = "Process blood pressure readings from Omron brand monitor")
parser.add_argument("clargs", nargs = 1, metavar = "Data_File.csv", type = str,
                     help = "File name of input data")

args = parser.parse_args()

if len(args.clargs) != 0:
     print("Data file is %s"%args.clargs[0])
filename = args.clargs[0]

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = csvreader.next() 

        print("Number of fields %d"%len(fields))

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names
for field in len(fields): 
        print("%s"%fields[field]) 

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') 

