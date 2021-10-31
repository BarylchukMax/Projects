import csv
import sys
filename1 = "1_gr.txt"
filename2 = "2_gr.txt"
fd = open(filename1, "r")
reader = csv.reader(fd, delimiter="\t")
for row in reader: 
 print(row) 
fd.close()