import time
from datetime import datetime
from tkinter import Tk

from pyautogui import alert


def scheduled_popup_flash_alert():
    set_alarm = input(f"Please enter alarm in HHMM format: ")
    description = input(f"Add optional description: ")
    try:
        time_from_str = datetime.strptime(set_alarm, '%H%M').time()
        now = datetime.now()
        alarm_time = datetime.combine(now.date(), time_from_str)
        print(alarm_time)
        if datetime.now() >= alarm_time:
            raise Exception('Please enter valid time!!')
        print(f"Setting alarm: {alarm_time}")
        total_seconds = (alarm_time - now).total_seconds()
        print(f"Sleeping for {total_seconds} seconds")
        time.sleep(total_seconds)

        for i in range(3):
            single_flash_tk()
        alert(title='~~~~~~~~~~~~~~~~~~~~~~ POPUP ALERT ~~~~~~~~~~~~~~~~~~~~~~',
              text=f'''
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              {f"{description}!!" if description else "GET READY!!"}
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ''', button='OK')
    except Exception as e:
        print(f"Something is wrong: {e}")


def single_flash_tk(color='red', delay=30):
    root = Tk()
    root.attributes("-topmost", True)
    root.configure(bg=color)
    root.overrideredirect(True)
    root.state('zoomed')
    root.after(delay, root.destroy)
    root.mainloop()


if __name__ == '__main__':
    scheduled_popup_flash_alert()
