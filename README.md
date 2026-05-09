# CSCI 7400 Comprehensive Exam Data Prep

This project contains a small Python workflow for cleaning and flattening YouTube trending data collected from multiple countries. It works with the raw CSV and JSON files in this repository and writes cleaned output into the `csv/corrected/` and `json/flattened/` folders.

## What it does

- `flatten csv.py` reads each country CSV file, checks row length against the header, appends a `country` column, and writes cleaned CSVs to `csv/corrected/`.
- `flatten json.py` reads each country category JSON file, extracts the `items` array, flattens the nested `snippet` fields, and writes one JSON object per line to `json/flattened/`.

## Project Context

This repository supports a CSCI 7400 comprehensive exam project analyzing global YouTube trending data with an AWS-based workflow. The report describes a pipeline built around:

- Amazon S3 for storage
- AWS Glue for cataloging and transformation
- Amazon Athena for SQL querying
- Amazon QuickSight for visualization
- IAM for access control

The report also notes that AWS Lambda was considered early on, but manual preprocessing and upload were used instead because the dataset is static and no YouTube API key was available.

The analysis focuses on 10 countries: US, RU, MX, KR, JP, IN, GB, FR, DE, and CA. It compares views, likes, dates, titles, and categories across those regions.

## Repository Layout

- Raw CSV files: `USvideos.csv`, `CAvideos.csv`, and the other country files in the project root
- Raw category JSON files: `US_category_id.json`, `CA_category_id.json`, and the other country files in the project root
- Cleaned CSV output: `csv/corrected/`
- Flattened JSON output: `json/flattened/`

## Requirements

- Python 3.x
- No third-party packages are required; both scripts use only the Python standard library

## How To Run

Both scripts currently use hardcoded `FOLDER_PATH` values that point to the original OneDrive archive location used by the author. Before running them locally, update the `FOLDER_PATH` and output folder constants in each script so they point to your local copy of this repository.

Then run:

```bash
python3 "flatten csv.py"
python3 "flatten json.py"
```

## Output Details

### CSV cleaning

The CSV script:

- reads every `.csv` file in the source folder
- validates each row has the same number of columns as the header
- adds a `country` column based on the first two characters of the filename
- skips malformed rows and prints them to the console

### JSON flattening

The JSON script:

- reads every `.json` file in the source folder
- extracts the `items` array
- converts nested `snippet` data into flat fields such as `snippet_channelId`, `snippet_title`, and `snippet_assignable`
- writes JSONL-style output, with one flattened object per line

## Notes

- The repository includes the cleaned output directories for convenience.
- If you want the scripts to run directly against this repository without editing paths, replace the hardcoded paths with relative paths first.
- The report's main findings were that categories 10 and 24 consistently had high engagement, GB had the highest average views in the summary table, and visualization choices could change how the same data looked when grouped differently.
