from tkinter import Tk

from pyautogui import alert


def single_flash_tk(color='red', delay=50):
    root = Tk()
    root.attributes("-topmost", True)
    root.configure(bg=color)
    root.overrideredirect(True)
    root.state('zoomed')
    root.after(delay, root.destroy)
    root.mainloop()


def popup_flash(description=None):
    for i in range(5):
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


if __name__ == '__main__':
    popup_flash()
