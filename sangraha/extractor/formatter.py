import json
import pandas as pd
import os


def csv_to_json(csv_file, output_file):

    df = pd.read_csv(csv_file)

    incidents = []

    for _, row in df.iterrows():

        incident = {
            "title": row["title"],
            "body": row["body"],
            "labels": row["labels"],
            "state": row["state"],
            "author": row["author"],
            "comments": row["comments"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
            "url": row["url"]
        }

        incidents.append(incident)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(incidents, f, indent=4, ensure_ascii=False)

    print(f"Saved {len(incidents)} incidents")