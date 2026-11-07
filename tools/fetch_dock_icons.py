import urllib.request
import re
import os

icons = {
    "netflix": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/netflix.svg",
    "primevideo": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/prime.svg",
    "hotstar": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/hotstar.svg",
    "disneyplus": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/disneyplus.svg",
    "playstation": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/playstation.svg",
    "youtube": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/youtube.svg",
    "appletv": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/appletv.svg",
}

out_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable"

def svg_to_vector_drawable(name, svg_text):
    # Extract path d attributes
    paths = re.findall(r'<path[^>]*d="([^"]+)"', svg_text)
    if not paths:
        print(f"No paths found for {name}")
        return
    
    xml_lines = [
        '<vector xmlns:android="http://schemas.android.com/apk/res/android"',
        '    android:width="48dp"',
        '    android:height="48dp"',
        '    android:viewportWidth="24"',
        '    android:viewportHeight="24">',
    ]
    for d in paths:
        xml_lines.append(f'    <path')
        xml_lines.append(f'        android:fillColor="#FFFFFFFF"')
        xml_lines.append(f'        android:pathData="{d}" />')
    xml_lines.append('</vector>\n')
    
    out_file = os.path.join(out_dir, f"ic_dock_{name}.xml")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    print(f"Created {out_file} with {len(paths)} paths.")

for name, url in icons.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode("utf-8")
            svg_to_vector_drawable(name, content)
    except Exception as e:
        print(f"Error fetching {name} from {url}: {e}")
        # Try alternate URL if prime fails
        if name == "primevideo":
            try:
                alt = "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/amazonprime.svg"
                with urllib.request.urlopen(urllib.request.Request(alt, headers={"User-Agent": "Mozilla/5.0"})) as resp:
                    svg_to_vector_drawable(name, resp.read().decode("utf-8"))
            except Exception as e2:
                print(f"Fallback also failed: {e2}")

