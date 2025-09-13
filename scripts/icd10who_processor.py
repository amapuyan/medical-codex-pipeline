import pandas as pd

file_path = 'input/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=':', header=None, names=columns, dtype=str, low_memory=False)

df = (
    df.loc[:, ['code', 'title_en']]
      .rename(columns={'title_en': 'description'})
      .assign(last_updated='09-06-2025')   
)[['code', 'description', 'last_updated']]

output_path = 'output/icd102019syst_codes.csv'
df.to_csv(output_path, index=False)

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"\nFirst 5 rows:")
print(df.head())
