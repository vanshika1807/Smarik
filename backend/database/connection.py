import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        return conn
    except Exception as e:
        print("Connection Failed!")
        print(e)
        return None