# Import os in order to interact with files on the esp.
import gc
import os

import esp
import network

# Turn off vendor OS debugging messages, in order to see only own debugging.
esp.osdebug(None)

# Run the garbage collector to reclaim memory occupied by objects that are no longer in use by the program.
# This is useful to save space in the flash memory
gc.collect()

# Network credentials. (Change to yours.)
ssid = 'PUT SSID HERE'
password = 'PUT PW HERE'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
# End network connection procedure (if we get here we can assume we're connected).