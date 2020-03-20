import csv

with open('./input/consumer_complaints.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  data = next(reader)
  print(data)



