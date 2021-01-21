#! /usr/bin/env python3

import time
import os

# config goes here
product_ID = "0x22a"
plist_name = "me.stevenconaway.KeyRemapping.plist"
# end config

while True:
    stream = os.popen(
        "hidutil property --matching '{\"ProductID\":" + product_ID + "}' --get \"UserKeyMapping\"")
    output = stream.read()

    if output.count("(null)") > 0:
        os.popen("launchctl unload ~/Library/LaunchAgents/" + plist_name +
                 " && launchctl load -w ~/Library/LaunchAgents/" + plist_name)

    time.sleep(5)
