import polars as pl
import pandas as pd
import time

npi_file_path = 'input/npidata_pfile_20050523-20250810.csv'

df = pl.read_csv(npi_file_path, n_rows=1000)




