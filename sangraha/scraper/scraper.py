import pandas as pd
import requests

def main():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    final = pd.DataFrame()

    for page in range(1, 11):

        url = f"https://api.github.com/repos/kubernetes/kubernetes/issues?state=all&per_page=100&page={page}"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed on page {page}")
            continue

        issues = response.json()

        title = []
        state = []
        created_at = []
        updated_at = []
        labels = []
        author = []
        comments = []
        body = []
        html_url = []

        for issue in issues:

            if "pull_request" in issue:
                continue

            title.append(issue.get("title"))
            state.append(issue.get("state"))
            created_at.append(issue.get("created_at"))
            updated_at.append(issue.get("updated_at"))
            author.append(issue["user"]["login"] if issue.get("user") else None)
            comments.append(issue.get("comments"))
            body.append(issue.get("body"))
            html_url.append(issue.get("html_url"))

            labels.append(
                ", ".join(label["name"] for label in issue.get("labels", []))
            )

        df = pd.DataFrame({
            "title": title,
            "state": state,
            "created_at": created_at,
            "updated_at": updated_at,
            "author": author,
            "comments": comments,
            "labels": labels,
            "body": body,
            "url": html_url
        })

        final = pd.concat([final, df], ignore_index=True)

    print(final.head())

    final.to_csv(
        "sangraha/output/kubernetes_incidents.csv",
        index=False
    )

    print("Scraping completed!")


if __name__ == "__main__":
    main()