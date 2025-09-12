import polars as pl
from pathlib import Path
from datetime import date

file_path = Path('input/RXNATOMARCHIVE.RRF')

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

df = pl.read_csv(
    file_path,
    separator='|',
    has_header = False,
    new_columns = columns,
    truncate_ragged_lines = True
)

# Add last_released column with a fixed date
df = df.with_columns([
    pl.lit('09-06-2025').alias('last_released')
])

# Rename columns to match desired output
df = df.rename({
    'str' : 'description',
})

# Keep only relevant columns and add last_updated column
df = (
    df.select(['code', 'description'])
    .with_columns(pl.lit(date.today().isoformat()).alias('last_updated'))
)

output_dlr = Path('output')
output_dlr.mkdir(exist_ok=True)
output_path = output_dlr / 'RXNATOARCHIVE.csv'

df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1042**2:.2f}")
