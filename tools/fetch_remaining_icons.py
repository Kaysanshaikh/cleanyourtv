import urllib.request
import re
import os

icons = {
    "prime": "https://raw.githubusercontent.com/homarr-labs/dashboard-icons/main/svg/prime-video.svg",
    "hotstar": "https://raw.githubusercontent.com/homarr-labs/dashboard-icons/main/svg/disney-plus.svg"
}

out_dir = r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\launcher\app\src\main\res\drawable"

for name, url in icons.items():
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode("utf-8")
        # Extract viewBox
        vb_match = re.search(r'viewBox="([^"]+)"', content)
        vb = vb_match.group(1).split() if vb_match else ["0", "0", "24", "24"]
        vw = vb[2] if len(vb) >= 4 else "24"
        vh = vb[3] if len(vb) >= 4 else "24"
        
        # Extract paths
        paths = re.findall(r'<path[^>]*d="([^"]+)"', content)
        xml_lines = [
            '<vector xmlns:android="http://schemas.android.com/apk/res/android"',
            f'    android:width="48dp"',
            f'    android:height="48dp"',
            f'    android:viewportWidth="{vw}"',
            f'    android:viewportHeight="{vh}">',
        ]
        for d in paths:
            xml_lines.append('    <path')
            xml_lines.append('        android:fillColor="#FFFFFFFF"')
            xml_lines.append(f'        android:pathData="{d}" />')
        xml_lines.append('</vector>\n')
        
        out_file = os.path.join(out_dir, f"ic_dock_{name}.xml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("\n".join(xml_lines))
        print(f"Created {out_file} with {len(paths)} paths.")

