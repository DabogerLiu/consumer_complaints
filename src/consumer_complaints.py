import csv
from datetime import timedelta

with open('./input/complaints.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  data = next(reader)
  print(data)



