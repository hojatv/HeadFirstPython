from datetime import datetime
import sys
import os
import time
import html

print(sys.version)
print(sys.platform)
print(os.getcwd())
print(os.environ)
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute


if right_this_minute in odds:
    print("This is odd minute  ...")
else:
    print("Not an odd minute  ...")

time.strftime("%H:%M")

print(html.escape("This HTML contains a <script>script</script> tag"))
print(html.unescape("I &hearts; python's &lt;standard library &gt;."))