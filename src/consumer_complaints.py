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

key1 = str(complains[0]['Product']) 
key2 = str(complains[0]['Date received'][0:4])
key = list()
key.append( key1 + key2)


for i in range(len(complains)):
  key.append(str(complains[i]['Product'])+str(complains[i]['Date received'][0:4]))

report = Counter(key).keys()
sorted_report = sorted(report)
product = list()
year = list()


for i in range(len(sorted_report)):
  year.append(sorted_report[i][0:4])
  product.append(sorted_report[i][4:])
  
Total_complains = list()
for i in range(len(report)):
  counter = 0
  for j in range(len(complains)):
    if (product[i]==complains[j]['Product'])&(year[i]==complains[j]['Date received'][0:4]):
      counter = counter+1
  Total_complains.append(counter)

ListsofCompany = []
for i in range(len(report)):
  company=[]
  for j in range(len(complains)):
    if (product[i] == complains[j]['Product'])&(year[i] == complains[j]['Date received'][0:4]):
      company.append(complains[j]['Company'])
  ListsofCompany.append(company)
Total_company = list()
Max_Frequency_Company = list()
for i in range(len(report)):
  Total_company.append(len(Counter(ListsofCompany[i]).keys()))
  #frequency  = list(Counter(ListsofCompany[i]).values())
  #max_frequency = max(frequency)  if frequency else None
  #max_frequency_company.append(round(max_frequency*100/Total_complains[i]))
  #Max_Frequency_Company.append(round(max(Counter(ListsofCompany[i]).values())*100/Total_complains[i]))
  

with open('./output/report.csv', 'w', newline='') as csvfile:
 # fieldnames = ['Product', 'Year','Total_complains','Total_company','max_frequency_company']
 fieldnames = ['Product', 'Year','Total_complains','Total_company']
  writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
  for i in range(len(report)):
    #writer.writerow({'Product':sorted_Product[i],'Year':sorted_Year[i],'Total_complains':sorted_Total_complains[i],'Total_company':sorted_Total_company[i],'sorted_max_frequency_company':sorted_max_frequency_company[i]})
    #writer.writerow({'Product':product[i].lower(),'Year':year[i],'Total_complains':Total_complains[i],'Total_company':Total_company[i],'max_frequency_company': Max_Frequency_Company[i]})
    writer.writerow({'Product':product[i].lower(),'Year':year[i],'Total_complains':Total_complains[i],'Total_company':Total_company[i]})
  #writer.writeheader()
