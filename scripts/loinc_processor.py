import pandas as pd

## 1000 rows due to memory constraints
loinc = pd.read_csv('input/Loinc.csv', nrows=1000)

loinc.info()

loinc.STATUS.value_counts()

loinc.iloc[0]

loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

loinc_small = loinc[list_cols]

loinc_small['last_updated'] = '09-06-2025'

loinc_small = loinc_small.rename(columns={
    'LOINC_NUM' : 'code' , 
    'LONG_COMMON_NAME' : 'description', 
})

file_output_path = 'output/loinc_small.csv'

loinc_small.to_csv('output/loinc_small.csv')

loinc_small.to_csv('output/loinc_small.csv', index=False)






