#
#
# must have secrets
import time
from adafruit_magtag.magtag import MagTag

magtag = MagTag(debug=True)
magtag.network.connect()

# Corresponds to time.localtime().tm_wday, with corresponding Monday.bmp, etc.
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print('we are connected yay')

timestamp = 0
day_of_week = 0

def update_display():
    daystr = days_of_week[ day_of_week ]
    print("update_display:",day_of_week, daystr)
    magtag.set_background("bmps/"+daystr+".bmp")
    magtag.refresh() 
    
    
while True:
    if time.monotonic() - timestamp > 60*60:  # resync time once an hour
        magtag.get_local_time()     # uses adafruit.io 
        timestamp = time.monotonic()
        print("updating!")

        now = time.localtime()
        day_of_week = now.tm_wday
        update_display()
        
    time.sleep(60*30)  # update infrequently
