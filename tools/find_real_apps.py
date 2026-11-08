import subprocess
import json

# Run adb command to test what ResolveInfo activities are returned
cmd = [
    r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\venv\Scripts\python.exe",
    r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv.py",
    "pm", "list", "packages", "-e"
]
p = subprocess.run(cmd, capture_output=True, text=True, env={"TV_HOST": "192.168.1.10"})
pkgs = [line.replace("package:", "").strip() for line in p.stdout.splitlines() if line.strip()]

# Test launch intents
launchable = []
for pkg in pkgs:
    # Check if package has LEANBACK_LAUNCHER or LAUNCHER
    c2 = [
        r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\venv\Scripts\python.exe",
        r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv.py",
        "dumpsys", "package", pkg
    ]
    p2 = subprocess.run(c2, capture_output=True, text=True, env={"TV_HOST": "192.168.1.10"})
    out = p2.stdout
    if "android.intent.category.LEANBACK_LAUNCHER" in out or "android.intent.category.LAUNCHER" in out:
        if "com.gathin.tvhome" not in pkg and "com.mitv" not in pkg and "com.xiaomi.mitv" not in pkg:
            launchable.append(pkg)

print("Actually installed launchable user apps:")
for l in launchable:
    print(" -", l)
