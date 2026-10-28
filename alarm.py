
import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("Wake up! Your alarm is ringing!")

        for i in range(5):
            print("🔔 ALARM! 🔔")
            time.sleep(1)

        break

    time.sleep(1)
