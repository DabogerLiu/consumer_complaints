import csv
from collections import Counter


def csv_dict_list(variables_file):
  # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs

  reader = csv.DictReader(open(variables_file))
  dict_list = []
  for line in reader:
    dict_list.append(line)
  return dict_list


complains = csv_dict_list('./input/consumer_complaints.csv')

#complains = csv_dict_list('C:/Users/Daboger/PycharmProjects/Insight_interview/complaints.csv')
report = {}
report[0] = {}
report[0]['Product']=complains[0]['Product']
report[0]['Year'] = complains[0]['Date received'][0:4]
report[0]['Total_complains'] = 1

i,j = 1,0
#print(len(report))
while (i < len(complains)):
  added = False
  for index in range(len(report)):
    if (report[index]['Product'] == complains[i]['Product'])&(report[index]['Year'] == complains[i]['Date received'][0:4]):
      report[index]['Total_complains'] = report[index]['Total_complains']+1
      added = True
      break
  if not added:            #Do not add 1
    j = j + 1
    report[j] = {}
    report[j]['Product']= complains[i]['Product']
    report[j]['Year']=complains[i]['Date received'][0:4]
    report[j]['Total_complains']=1
  i = i+1

ListsofCompany = []
for i in range(len(report)):
  company=[]
  for j in range(len(complains)):
    if (report[i]['Product'] == complains[j]['Product'])&(report[i]['Year'] == complains[j]['Date received'][0:4]):
      company.append(complains[j]['Company'])
  ListsofCompany.append(company)

for i in range(len(report)):
  report[i]['Total_company']= len(Counter(ListsofCompany[i]).keys())
  report[i]['max_frequency_company'] = round(max(Counter(ListsofCompany[i]).values())*100/report[i]['Total_complains'])

Product = list()
Year = list()
Total_complains = list()
Total_company = list()
max_frequency_company = list()
for i in range(len(report)):
  Product.append(report[i]['Product'])
  Year.append(report[i]['Year'])
  Total_complains.append(report[i]['Total_complains'])
  Total_company.append(report[i]['Total_company'])
  max_frequency_company.append(report[i]['max_frequency_company'])
#sorted_Product = sorted(Product)
#print(sorted_Product)
sorted_index = sorted(range(len(Product)),key=Product.__getitem__)  #get the index list

sorted_Product = sorted(Product)

sorted_Year = list()
sorted_Total_complains = list()
sorted_Total_company = list()
sorted_max_frequency_company = list()

for index in range(len(report)):
  sorted_Year.append(Year[sorted_index[index]])
  sorted_Total_complains.append(Total_complains[sorted_index[index]])
  sorted_Total_company.append(Total_company[sorted_index[index]])
  sorted_max_frequency_company.append(max_frequency_company[sorted_index[index]])

for i in range(len(report)):
  print(sorted_Product[i],sorted_Year[i], sorted_Total_complains[i],sorted_Total_company[i],sorted_max_frequency_company[i])

with open('./output/report.csv', 'w', newline='') as csvfile:
  fieldnames = ['Product', 'Year','Total_complains','Total_company','sorted_max_frequency_company']
  writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
  for i in range(len(report)):
    writer.writerow({'Product':sorted_Product[i], 'Year':sorted_Year[i],'Total_complains':sorted_Total_complains[i],'Total_company':sorted_Total_company[i],'sorted_max_frequency_company':sorted_max_frequency_company[i]})
    #writer.writerow({sorted_Product[i],sorted_Year[i], sorted_Total_complains[i],sorted_Total_company[i],sorted_max_frequency_company[i]})
  #writer.writeheader()
