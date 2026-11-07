import urllib.request
import re
from PIL import Image

url = "https://docs.google.com/document/u/0/d/1JrGoSIpS25907k3UYvtLf_s34vReFVZV/mobilebasic?pli=1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8")
    img_urls = re.findall(r'<img[^>]+src="([^">]+)"', html)

for i in [3, 4]:
    base_u = img_urls[i].split("=")[0]
    full_u = base_u + "=s1920"
    print(f"Fetching {i} at full res: {full_u[:80]}")
    with urllib.request.urlopen(urllib.request.Request(full_u, headers={"User-Agent": "Mozilla/5.0"})) as r:
        data = r.read()
        path = f"doc_images/full_{i}.png"
        with open(path, "wb") as f:
            f.write(data)
        im = Image.open(path)
        print(f"Success! {path} size is {im.size}")

