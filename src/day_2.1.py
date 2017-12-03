#!/usr/bin/python3

import csv

with open("spreadsheet.csv") as infile:
	reader = csv.reader(infile, delimiter="\t")

	checksum = 0
	for row in reader:
		row = list(map(int, row))
		checksum += max(row) - min(row)

print(checksum)