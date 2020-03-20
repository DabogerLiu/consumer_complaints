import numpy as np
import pandas as pd

data_dir =  "C:/Users/Daboger/PycharmProjects/Insight_interview/"
complains = pd.read_csv(data_dir+'complaints.csv')

complains['Date received'] =  pd.to_datetime(complains['Date received']).dt.to_period('Y')
def max_percent(x):
    return np.around(100 * x.value_counts().max()/x.count())
report = complains.groupby(['Product','Date received']).agg(
    {

        'Product':'size',
        'Company': ['nunique',max_percent]
    }
)
print(report)
report.reset_index().to_csv (r'C:/Users/Daboger/PycharmProjects/Insight_interview/report.csv', index = False, header=False)


