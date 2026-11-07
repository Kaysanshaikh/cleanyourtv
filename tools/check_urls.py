import urllib.request
import re

url = "https://docs.google.com/document/u/0/d/1JrGoSIpS25907k3UYvtLf_s34vReFVZV/mobilebasic?pli=1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8")
    img_urls = re.findall(r'<img[^>]+src="([^">]+)"', html)
    for i, u in enumerate(img_urls):
        print(f"URL {i}:", u[:100])

