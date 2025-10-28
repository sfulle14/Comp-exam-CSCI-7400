import os
import csv

FOLDER_PATH = "/Users/stevenfuller/Library/CloudStorage/OneDrive-MiddleTennesseeStateUniversity/comprehensive exam/csci 7400/archive/"
CLEANED_FOLDER = "/Users/stevenfuller/Library/CloudStorage/OneDrive-MiddleTennesseeStateUniversity/comprehensive exam/csci 7400/archive/csv/corrected/"
os.makedirs(CLEANED_FOLDER, exist_ok=True)

for filename in os.listdir(FOLDER_PATH):
    if filename.endswith('.csv'):
        filepath = os.path.join(FOLDER_PATH, filename)
        country_code = filename[:2].upper()  # Extract first two letters of the filename as country code
        print(f"\nChecking file: {filename} (Country: {country_code})")

        cleaned_rows = []

        try:
            with open(filepath, encoding='utf-8', errors='replace') as f:
                reader = csv.reader(f)
                try:
                    header = next(reader)
                    expected_columns = len(header)
                    header.append('country')
                    cleaned_rows.append(header)
                except Exception as e:
                    print(f"Failed to read header: {e}")
                    continue

                for i, row in enumerate(reader, start=2):  # start=2 to account for header
                    if len(row) != expected_columns:
                        print(f"Bad row at line {i}: {row}")
                    else:
                        row.append(country_code)
                        cleaned_rows.append(row)

            # Save cleaned file
            cleaned_path = os.path.join(CLEANED_FOLDER, filename)
            with open(cleaned_path, 'w', newline='', encoding='utf-8') as f_out:
                writer = csv.writer(f_out)
                writer.writerows(cleaned_rows)
                print(f"Saved cleaned file to: {cleaned_path}")
        except Exception as e:
            print(f"Failed to process file {filename}: {e}")
