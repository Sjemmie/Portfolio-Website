import requests
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com"


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("temp.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    with open("temps.txt", "a") as file:
        timestamp = str(datetime.now().replace(microsecond=0))
        return file.write(timestamp + ", " + extracted + "\n")


def run():
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(extracted)
