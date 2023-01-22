import requests
import time
import subprocess

"""
This script uses the requests library to check the website, and the 
subprocess library to run the AppleScript command that displays the notification. 
The script will run indefinitely and check the website every minute. 
If you want to stop the script, you need to manually interrupt it.
"""

# Website to monitor
url = "https://ohq.io/courses/531"

while True:
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        time.sleep(60)
        continue
    if "Queue Closed" not in response.text:
        # Show banner notification
        subprocess.run(["osascript", "-e", 'display notification "Queue is open!" with title "OHQ Status"'])
        break
    time.sleep(60)