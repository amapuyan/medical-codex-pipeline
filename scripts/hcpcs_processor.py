import pandas as pd

file_path = 'input/HCPC2025_OCT_ANWEB_v3.txt'

colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "code", "description_1", "description_2", "type", 
    "unknown_1", "unknown_2", "unknown_3", "unknown_4"
]

df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)

output_path = 'output/hcpcs_data.csv'
df.to_csv(output_path, index=False)

