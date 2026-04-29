import time
from plyer import notification

reminder_interval_seconds = int(input("Enter reminder interval in seconds: "))

while True:
    notification.notify(
        title="Water Reminder",
        message="Please drink some water to stay hydrated.",
        timeout=5,
    )

    time.sleep(reminder_interval_seconds)
