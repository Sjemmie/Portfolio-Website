import requests
import selectorlib
from sendmail import send_email
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"
connection = sqlite3.connect("data.db")


def scrape(url):
    """"Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    data = extracted.split(",")
    data = [item.strip() for item in data]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", data)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? and date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                send_email(extracted)
                store(extracted)
        time.sleep(2)
