import requests
API_KEY = "44d37faecb38d51c04e31300fd9540cd651f9"

url = input()

api_url = f"https://cutt.ly/api/api.php?key={API_KEY}&short={url}"
#api_url = f"https://cutt.ly/api/api.php?key="+API_KEY+"&short="+url
print(api_url)

data = requests.get(api_url).json()["url"]
if data["status"]==7:
    short_url = data["shortLink"]
    print(short_url)
else:
    print("error")
print(data)