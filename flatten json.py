import os
import json

FOLDER_PATH = "/Users/stevenfuller/Library/CloudStorage/OneDrive-MiddleTennesseeStateUniversity/comprehensive exam/csci 7400/archive/"
CLEANED_FOLDER = "/Users/stevenfuller/Library/CloudStorage/OneDrive-MiddleTennesseeStateUniversity/comprehensive exam/csci 7400/archive/json/flattened/"
os.makedirs(CLEANED_FOLDER, exist_ok=True)

for filename in os.listdir(FOLDER_PATH):
    if filename.endswith(".json"):
        with open(os.path.join(FOLDER_PATH, filename), "r", encoding="utf-8") as f:
            try:
                # Step 1: Load entire file
                original_json = json.load(f)

                # Step 2: Extract items list
                items = original_json.get("items", [])

                # Step 3: Output one flattened object per line
                target_path = os.path.join(CLEANED_FOLDER, filename)
                with open(target_path, "w", encoding="utf-8") as out_f:
                    for item in items:
                        if isinstance(item, dict):
                            snippet = item.get("snippet", {})
                            flat_item = {
                                "id": item.get("id"),
                                "kind": item.get("kind"),
                                "etag": item.get("etag"),
                                "snippet_channelId": snippet.get("channelId"),
                                "snippet_title": snippet.get("title"),
                                "snippet_assignable": snippet.get("assignable")
                            }
                            json.dump(flat_item, out_f)
                            out_f.write("\n")
                print(f"Converted: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
