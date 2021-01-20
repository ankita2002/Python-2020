import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()
while (True):
    percentage = battery.percent
    notification.notify(
        title="Battery Percentage",
        message=str(percentage)+"% Battery left",
        timeout=10
    )
    time.sleep(60*60)
    continue