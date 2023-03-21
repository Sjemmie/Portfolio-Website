import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com"
connection = sqlite3.connect("tempdata.db")


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("temp.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    timestamp = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Temperatus VALUES(?,?)", (timestamp, extracted))
    connection.commit()


scraped = scrape(URL)
extracted = extract(scraped)
store(extracted)
