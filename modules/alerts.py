import tkinter as tk
from threading import Timer
from win32api import GetSystemMetrics


class Alert(object):
    """
    Modifed alert box
    """
    def __init__(self):

        def translate():
            """
            This function calculates the size of the screen and the size of the window for positioning
            :return: tuple (c_x, c_y)
            """
            tr_x, tr_y = self.screen_size[0] - self.WinSize[0], self.screen_size[1] - self.WinSize[1]
            return tr_x // 2, tr_y // 2

        # Settings
        self.WinSize = (700, 400)       # Alert Size
        self.WinBg = "gray20"
        self.ov = 1     # CP index:: <0> - on; <1> - off

        # Header
        self.header_font = "@Microsoft YaHei Light"
        self.header_size = 28
        self.header_fg = "white"
        self.wrap_index = 35    # Wrap

        # Alert
        self.alert = tk.Tk()
        self.screen_size = self.alert.winfo_screenwidth(), self.alert.winfo_screenheight()  # getting screen metrics
        self.transform = translate()
        self.alert.geometry(f'{self.WinSize[0]}x{self.WinSize[1]}+{self.transform[0]}+{self.transform[1]}')     # Placing window
        self.alert.configure(bg=self.WinBg)     # setting background
        self.alert.overrideredirect(self.ov)    # Disable control panel
        self.alert.wm_attributes("-topmost", True)  # topmost >> True

    def Show(self, **kwargs):
        def type_writing(index, speed, wrap_index):
            """
            Type writing
            <?>Text wrapping</?>
            """
            try:
                # Inserting cymble
                header['text'] += kwargs['text'][index]

                # Text Wrapping >> placing
                if len(header['text']) >= wrap_index:
                    header['text'] += "\n"
                    self.wrap_index += self.wrap_index

                # Starting timer if not index error
                Timer(speed, type_writing, args=(index + 1, speed, self.wrap_index)).start()
            except IndexError:
                pass

        # Creating header widget >> <label>
        header = tk.Label(self.alert, font=(self.header_font, self.header_size), fg=self.header_fg)
        header.configure(bg=self.WinBg)
        header.place(x=0, y=0)

        # Starting writing
        type_writing(0, kwargs['speed'], self.wrap_index)
        self.alert.after(kwargs['delay'], lambda: self.alert.destroy())     # Closing window if screen time ended

        # Loop
        self.alert.mainloop()


class WinLocker(object):
    """
    Screenlocker
    """
    def __init__(self):

        def disable_closing():
            pass

        # Config
        self.WinSize = [GetSystemMetrics(i) for i in range(2)]
        self.WinBg = "gray20"

        # Window
        self.win_locker = tk.Tk()   # creating window
        self.win_locker.wm_protocol("WM_DELETE_WINDOW", disable_closing)    # disabling window closing
        self.win_locker.overrideredirect(1)     # No control panel
        self.win_locker.wm_attributes("-topmost", True)     # topmost showing
        self.win_locker.geometry(f'{self.WinSize[0]}x{self.WinSize[1]}')    # setting geometry

    def Lock(self, **kwargs):
        # This function locks screen, it can't be closed without command from admin
        self.win_locker.configure(bg=kwargs['background'])
        self.win_locker.after(kwargs['delay'], lambda: self.win_locker.destroy())   # Destroying window
        self.win_locker.mainloop()
