import requests
from send_email import send_email


api_key = "2074a7c40a0d49688be216c5e42c6db8"

url = "https://newsapi.org/v2/everything?q=tesla&from=2"\
      "024-01-21&sortBy=publishedAt&apiKey=2074a7c40a0d496"\
      "88be216c5e42c6db8"

# Made Request to get api
request = requests.get(url)
# Converted api to dictionary
content = request.json()

# Accessing description and title
body = ""
for article in content["articles"]:
    """
    if article["description"] is not None:
    (or)
    """
    try:
        body = body + article["title"] + "\n" + article["description"]
    except TypeError:
        continue

body = body.encode("utf-8")
send_email(body)







