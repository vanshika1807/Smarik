import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(os.environ["DATABASE_URL"])

with open("backend/database/schema.sql", "r") as file:
    schema = file.read()

cur = conn.cursor()

cur.execute(schema)

conn.commit()

print("Incidents table created successfully!")

cur.close()
conn.close()