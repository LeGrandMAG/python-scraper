#program to scrape image from a Unsplash


import requests
url = "https://unsplash.com/napi/search?query=dog&per_page=20&xp=search-multi-word%3A"
r = requests.get(url)

data = r.json()


for item in data['photos']['results']:
    name = item['id']
    urls = item['urls']['regular']
    with open(name +'.jpg','wb') as f:
        f.write(requests.get(urls).content)