"""
This module controls shell
"""

from sys import argv
from os import path, getcwd
from subprocess import call


def call_command(command):
    """
    This function calls shell command
    :param command: Shell command : str
    :return:
    """
    try:
        print(command)
        call(command)
        return f'"{command}" was executed.'
    except Exception as e:
        return e


def startup():
    """
    This function adds main executable file to thme system startup
    :return: log, if failed returning error
    """
    try:
        pattern =[r"REG ADD \"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\" /v ", " /t REG_SZ /f /d "]   # patterns
        file_name = path.basename(argv[0])  # getting filename
        full_path = f'{getcwd()}\\{file_name}'     # generating filepath
        command = f'{pattern[0]}"{file_name}"{pattern[1]}"{full_path}"'
        call(command)
        return f'"{full_path}" added to startup.'
    except Exception as e:
        return e


def shutdown():
    """
    System shutdown
    :return:
    """
    try:
        call("shutdown -s /t 0 /f")
    except Exception as e:
        return e


def restart():
    """
    System restart
    :return:
    """
    try:
        call("shutdown -r /t 0 /f")
    except Exception as e:
        return e
