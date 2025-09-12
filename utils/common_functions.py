def save_to_formats(df, base_filename):
	# Example: save as CSV and Excel
	df.to_csv(f"{base_filename}.csv", index=False)
	df.to_excel(f"{base_filename}.xlsx", index=False)

save_to_formats(df, base_filename)
