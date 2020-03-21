import csv
import dateutil.parser as parser

with open('./input/complaints.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  data = next(reader)
  print(data)



