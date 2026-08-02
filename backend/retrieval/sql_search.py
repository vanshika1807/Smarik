import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def search_incidents(keyword):

    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()

    query = """
        SELECT
            title,
            state,
            author,
            github_url
        FROM incidents
        WHERE
            title ILIKE %s
            OR description ILIKE %s
        LIMIT 10;
    """

    cur.execute(query, (f"%{keyword}%", f"%{keyword}%"))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


if __name__ == "__main__":

    keyword = input("Enter keyword: ")

    results = search_incidents(keyword)

    if len(results) == 0:
        print("No incidents found.")
    else:
        for row in results:
            print("=" * 80)
            print("Title :", row[0])
            print("State :", row[1])
            print("Author:", row[2])
            print("URL   :", row[3])