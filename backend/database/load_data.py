import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.environ["DATABASE_URL"])
cur = conn.cursor()

with open("sangraha/output/json/kubernetes_incidents.json", "r", encoding="utf-8") as f:
    incidents = json.load(f)

count = 0

for incident in incidents:

    cur.execute("""
        INSERT INTO incidents (
            title,
            description,
            state,
            author,
            labels,
            comments,
            created_at,
            updated_at,
            github_url
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (github_url) DO NOTHING;
    """, (
        incident.get("title"),
        incident.get("body"),
        incident.get("state"),
        incident.get("author"),
        incident.get("labels", []),
        incident.get("comments"),
        incident.get("created_at"),
        incident.get("updated_at"),
        incident.get("url")
    ))

    count += 1

conn.commit()

print(f"Inserted {count} incidents")

cur.close()
conn.close()