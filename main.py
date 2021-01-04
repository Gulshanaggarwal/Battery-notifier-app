from plyer import notification,battery
import time
while(True):
    current_percent=battery.status    # current_percent(type list)

    # check when battery is less than 35 percent

    if current_percent['percentage']<35:
        final_message="Current battery "+str(current_percent['percentage'])+"%"
        notification.notify(
            title="Battery notifier",
            message=final_message,
            timeout=10
        )
        time.sleep(60*20)

    # check when battery is less than 25 percent

    if current_percent['percentage']<=25:
        final_message="Current battery "+str(current_percent['percentage'])+"%"+"\n bro! charge your laptop immediately or stop working"
        notification.notify(
            title="Battery notifier\n Warning!",
            message=final_message,
            timeout=10
        )
        time.sleep(60)

    # else part

    else:
        final_message = "Current battery " + str(current_percent['percentage'])+"%" +"\n keep working bro!"
        notification.notify(
            title="Battery notifier",
            message=final_message,
            timeout=10
        )
        time.sleep(60*45)

