#!/usr/bin/python3

import csv

with open("spreadsheet.csv") as infile:
	reader = csv.reader(infile, delimiter="\t")

	sum_of_divisions = 0
	for row in reader:
		row = sorted(map(int, row), reverse=True)

		for idx, num in enumerate(row):
			for smaller_num in row[idx+1:]:
				if num % smaller_num == 0:
					sum_of_divisions += num // smaller_num

print(sum_of_divisions)