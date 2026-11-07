import urllib.request
import re

url = "https://hdqwalls.com/doctor-doom-1920x1080-wallpaper"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
        imgs = re.findall(r'src="([^"]*doctor-doom[^"]*\.jpg)"', html)
        print("Found images:", imgs[:5])
        links = re.findall(r'href="([^"]*doctor-doom[^"]*)"', html)
        print("Found links:", links[:5])
except Exception as e:
    print("Error:", e)

