import subprocess
import os

env = os.environ.copy()
env["TV_HOST"] = "192.168.1.10"
res = subprocess.run(
    [r"cleanyourtv\tools\venv\Scripts\python.exe", r"cleanyourtv\tools\tv.py", "pm list packages"],
    env=env, capture_output=True, text=True
)

for line in res.stdout.splitlines():
    for word in ["netflix", "amazon", "hotstar", "youtube", "apple", "mxtech", "mitv", "hdmi"]:
        if word in line.lower():
            print(line)

