import requests

url = "https://shanghai.zbj.com/search/f/?kw=SAAS"
response = requests.get(url)
print(response.text)