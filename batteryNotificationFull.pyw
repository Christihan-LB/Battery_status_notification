
import psutil
import time
from win10toast import ToastNotifier

# from psutil we will import the
# sensors_battery class and with
# that we have the battery remaining
toast = ToastNotifier()
l_percents=[70,75,80,85,90,95,100]
while(True):
    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        power_plugged = battery.power_plugged
        #print(power_plugged, percent)
        if power_plugged==True and (percent in l_percents):
            #print("Entró")
            toast.show_toast(
                "Battery Percentage",
                "Battery reach " + str(percent) + " %",
                duration = 60,
                icon_path = r"C:\Users\chris\OneDrive\Imágenes\icon.ico",
                threaded = False,
            )
            while toast.notification_active():
              time.sleep(0.1)
        #time.sleep(5)
    continue
