import re

# 1. Fix Prime Video
with open(r"cleanyourtv\launcher\app\src\main\res\drawable\ic_dock_prime.xml", "r") as f:
    prime_xml = f.read()

# Replace viewport
prime_xml = re.sub(r'android:viewportWidth="[^"]+"', 'android:viewportWidth="800.3"', prime_xml)
prime_xml = re.sub(r'android:viewportHeight="[^"]+"', 'android:viewportHeight="246.3"', prime_xml)

with open(r"cleanyourtv\launcher\app\src\main\res\drawable\ic_dock_prime.xml", "w") as f:
    f.write(prime_xml)
print("Updated ic_dock_prime.xml viewport to 800.3 x 246.3")

# 2. Fix Hotstar / Starburst:
# The starburst logo is a clean 4-pointed star:
hotstar_star = """<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="48dp"
    android:height="48dp"
    android:viewportWidth="100"
    android:viewportHeight="100">
    <!-- Starburst 4-pointed sparkle matching doc Section 5 -->
    <path
        android:fillColor="#FFFFFFFF"
        android:pathData="M50,0 C51,35 65,49 100,50 C65,51 51,65 50,100 C49,65 35,51 0,50 C35,49 49,35 50,0 Z" />
    <path
        android:fillColor="#FFFFFFFF"
        android:pathData="M50,22 C50.5,40 60,49.5 78,50 C60,50.5 50.5,60 50,78 C49.5,60 40,50.5 22,50 C40,49.5 49.5,40 50,22 Z" />
</vector>
"""
with open(r"cleanyourtv\launcher\app\src\main\res\drawable\ic_dock_hotstar.xml", "w") as f:
    f.write(hotstar_star)
print("Updated ic_dock_hotstar.xml to clean starburst vector")

