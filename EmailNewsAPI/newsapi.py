import requests
from sendmail import send_email

topic = "tesla"
api_key = "3632e02bcce54cf499ce95e05d04c54a"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2023-01-28" \
      "&sortBy=publishedAt" \
      "&apiKey=3632e02bcce54cf499ce95e05d04c54a" \
      "&language=en"

request = requests.get(url)
content = request.json()

body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    body = body + str(article["title"]) + "\n" \
           + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
