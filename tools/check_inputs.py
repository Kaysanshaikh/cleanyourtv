import subprocess
import os

env = os.environ.copy()
env["TV_HOST"] = "192.168.1.10"
res = subprocess.run(
    [r"cleanyourtv\tools\venv\Scripts\python.exe", r"cleanyourtv\tools\tv.py", "dumpsys tv_input"],
    env=env, capture_output=True, text=True
)

for line in res.stdout.splitlines():
    if "hdmi" in line.lower() or "input" in line.lower():
        print(line)

