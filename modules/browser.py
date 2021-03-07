"""
Browser control module
"""


from webbrowser import open as open_url


def OpenLink(url, count):
    """
    :param url: Url : str
    :param count: int
    :return: None
    """
    try:
        for i in range(count):
            open_url(url)

        return "Finished"
    except Exception as e:
        return e


