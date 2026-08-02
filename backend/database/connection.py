import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(os.environ["DATABASE_URL"])

print("connected to CockroachDB")

with conn.cursor() as cur:
    cur.execute("SELECT NOW();")
    print(cur.fetchone())

conn.close()