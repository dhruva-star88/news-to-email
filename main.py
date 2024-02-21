import requests

api_key = "2074a7c40a0d49688be216c5e42c6db8"

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-21&sortBy=publishedAt&apiKey=2074a7c40a0d49688be216c5e42c6db8"

# Made Request to get api
request = requests.get(url)
# Converted api to dictionary
content = request.json()

# Accessing description and title
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
