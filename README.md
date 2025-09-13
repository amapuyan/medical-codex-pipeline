# Medical-Codex-Pipeline Assignment Module 1
**HHA 507 Data Science Health Informatics 2025**

# Overview
This repository contains the assignment to ingest official code sets (LOINC, RxNorm, SNOMED CT, ICD-10 WHO, ICD-10CM, NPI, HCPCS), standardize them to a minimal schema, and export clean files for analysis.

# Structure
medical-codex-pipeline/
├── input/
├── scripts/
│   ├── snomed_processor.py
│   ├── icd10cm_processor.py
│   ├── icd10who_processor.py
│   ├── hcpcs_processor.py
│   ├── loinc_processor.py
│   ├── rxnorm_processor.py
│   └── npi_processor.py
├── output/
│   ├── csv/
├── utils/
│   └── common_functions.py
├── requirements.txt
└── README.md

**Target schema (all outputs):**
- `code`
- `description`
- `last_updated`

# (Steps)
1. **Set up project & venv**: created `.venv`, installed `pandas`/`polars`.
2. **Common utility**: added `utils/common_functions.py` with `save_to_formats(df, name)` to save CSVs (UTF-8, no index) into `/output`.
3. **LOINC** (`scripts/loinc_processor.py`):
   - Read `input/Loinc.csv`
   - Selected/renamed to `code`, `description`, `last_updated`
   - Saved to `output/loinc_standardized.csv`
4. **RxNorm** (`scripts/rxnorm_processor.py`):
   - Read pipe-delimited `input/RXNATOMARCHIVE.RRF` (no header) with Polars
   - Mapped `str → description`, kept `code`
   - Added `last_updated`
   - Saved to `output/rxnorm_min.csv`
5. **SNOMED CT** (`scripts/snomed_processor.py`):
   - Read tab-delimited `input/sct2_Description_Full-*.txt` with Polars
   - (Optional) filtered by `effectiveTime` date
   - Selected/renamed `id/id:` → `code`, `term` → `description`, formatted/assigned `last_updated`
   - Saved to `output/snomed_description_min.csv` (Parquet optional)
6. **ICD-10 WHO** (`scripts/icd10who_processor.py`):
   - Read colon-delimited `input/icd102019syst_codes.txt` with pandas
   - Chose `title_en` as `description`, kept `code`, added `last_updated`
   - Saved to `output/icd10who_min.csv`
7. **ICD-CM** (`scripts/icd10cm_processor.py`):
   - Read ICD-CM file from `input/` (e.g., ICD-10-CM release), mapped `code` and preferred description → `description`, used the effective/release date (or fixed date) for `last_updated`, saved to `output/icd10cm_codes.csv`
8. **NPI** (`scripts/npi_processor.py`):
   - Read NPPES NPI data from `input/`, selected `NPI` → `code` and a human-friendly name field (e.g., provider org or individual name) → `description`, set `last_updated`, saved to `output/npi_small.csv`
9. **HCPCS** (`scripts/hcpcs_processor.py`):
   - Read the HCPCS file from `input/`, selected `code` and the short/long description field → `description`, set `last_updated`, saved to `output/hcpcs_data.csv`
   