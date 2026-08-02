from scraper.scraper import main as scrape
from extractor.formatter import csv_to_json

if __name__ == "__main__":

    scrape()

    csv_to_json(
        "sangraha/output/kubernetes_incidents.csv",
        "sangraha/output/json/kubernetes_incidents.json"
    )

    print("Pipeline completed!")