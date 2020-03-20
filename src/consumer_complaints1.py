import pandas as pd

complains = pd.read_csv('./input/consumer_complaints.csv')

complains['Date received'] =  pd.to_datetime(complains['Date received']).dt.to_period('Y')
def max_percent(x):

    result=100 * x.value_counts().max()/x.count()

    return round(result)
report = complains.groupby(['Product','Date received']).agg(
    {

        'Product':'size',
        'Company': ['nunique',max_percent]
    }
)
print(report)
report.reset_index().to_csv (r' ./output/report.csv', index = False, header=False)


