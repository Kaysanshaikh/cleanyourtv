import subprocess

test_pkgs = [
    "com.android.vending",
    "com.mxtech.videoplayer.television",
    "com.yablio.sendfilestotv",
    "com.apple.atve.androidtv.appletv",
    "in.startv.hotstar",
    "com.amazon.amazonvideo.livingroom",
    "com.netflix.ninja",
    "com.google.android.youtube.tv",
    "com.android.tv.settings",
    "com.sonyliv",
    "com.jio.media.stb.ondemand.xiaomi",
    "com.graymatrix.did"
]

for p in test_pkgs:
    c = [
        r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\venv\Scripts\python.exe",
        r"c:\Users\Kaysan Shaikh\Desktop\Claude\cleanyourtv\tools\tv.py",
        "dumpsys", "package", p
    ]
    res = subprocess.run(c, capture_output=True, text=True, env={"TV_HOST": "192.168.1.10"})
    out = res.stdout
    enabled = "enabled=0" not in out and "enabled=3" not in out and "Package [" in out
    has_launcher = "android.intent.category.LEANBACK_LAUNCHER" in out or "android.intent.category.LAUNCHER" in out
    print(f"{p}: installed={('Package [' in out)}, enabled={enabled}, launcher={has_launcher}")
