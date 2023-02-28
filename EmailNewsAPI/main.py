import requests

api_key = "3632e02bcce54cf499ce95e05d04c54a"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-01-28&sortBy=publishedAt&apiKey=3632e02bcce54cf499ce95e05d04c54a"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])