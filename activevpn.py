#! /usr/bin/python

import time, sys
import scrollphat
from datetime import datetime

while True:

  vpnlog = open('/var/log/openvpn-status.log')

  x = 0
  msg = ""

  for line in vpnlog:
        x += 1
        if x < 4:
                continue

        if "ROUTING TABLE" in line:
                break
        else:
                userlist = (line.split(","))
                name = userlist[0]
                connect_time = userlist[4].replace("\n", "")
                connect_time = datetime.strptime(connect_time, '%c')
                time_now = datetime.now()
                connected = time_now - connect_time
                connected = str(connected).split('.', 2)[0]
                msg += (name.upper() + " SESSION TIME: " + connected + " ")

  vpnlog.close()

  scrollphat.set_brightness(25)
  scrollphat.write_string(msg, 11)
  length = scrollphat.buffer_len()

  for i in range(length): # for one off's
        try:
                scrollphat.scroll(1)
                time.sleep(0.06)
                msg = " "
        except KeyboardInterrupt:
                scrollphat.clear()
                sys.exit(-1)

  # clear the phat buffer and sleep for 30 seconds
  scrollphat.clear()
  time.sleep(30)
  
