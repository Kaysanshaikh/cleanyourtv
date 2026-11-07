import urllib.request
import json
import re

url = "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/_data/simple-icons.json"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

for item in data.get("icons", []):
    title = item.get("title", "").lower()
    slug = item.get("slug", "")
    if any(k in title for k in ["prime", "amazon", "hotstar", "disney"]):
        print(f"Title: {item.get('title')} -> Slug: {slug}")

