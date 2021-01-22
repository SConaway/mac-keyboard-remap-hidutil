#! /usr/bin/env python3

import time
import os

time.sleep(60)

# config goes here
product_ID = "0x22a"
plist_name = "me.stevenconaway.KeyRemapping.plist"
# end config

# os.popen("osascript -e 'display notification \"hello world!\"'")

while True:
#     print("loop start")
    stream = os.popen(
        "hidutil property --matching '{\"ProductID\":" + product_ID + "}' --get \"UserKeyMapping\"")
    output = stream.read()
#     os.popen("touch /Users/steven/keyb")

    if output.count("(null)") > 0:
#         print("reloading...")
        os.popen("launchctl unload ~/Library/LaunchAgents/" + plist_name +
                 " && launchctl load -w ~/Library/LaunchAgents/" + plist_name)

    
    time.sleep(5)
#     print("loop done")
