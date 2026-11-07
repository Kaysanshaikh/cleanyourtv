import urllib.request
import re
import os

url = "https://docs.google.com/document/u/0/d/1JrGoSIpS25907k3UYvtLf_s34vReFVZV/mobilebasic?pli=1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
        print("Doc HTML length:", len(html))
        img_urls = re.findall(r'<img[^>]+src="([^">]+)"', html)
        print("Found", len(img_urls), "images in the doc!")
        os.makedirs("doc_images", exist_ok=True)
        for i, u in enumerate(img_urls):
            # Clean url
            u_clean = u.replace("&amp;", "&")
            try:
                img_req = urllib.request.Request(u_clean, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(img_req) as img_resp:
                    data = img_resp.read()
                    out_path = f"doc_images/img_{i}.jpg"
                    with open(out_path, "wb") as f:
                        f.write(data)
                    print(f"Saved img_{i}.jpg: {len(data)} bytes")
            except Exception as e2:
                print(f"Failed img_{i}: {e2}")
except Exception as e:
    print("Failed to fetch doc:", e)

