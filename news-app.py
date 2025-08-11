import requests

Query =input("What news are you interested in:")
ApiKey = "c0351d814f2744619be67a58ef91664c"

url = f"https://newsapi.org/v2/everything?q={Query}&from=2025-07-11&sortBy=publishedAt&apiKey={ApiKey}"

print(url)
c = requests.get(url)
data = c.json()
articles = data["articles"] 
for index , article in enumerate(articles):
    print(index + 1 , article["title"] , article["url"])
    print("\n************************************\n")
    
