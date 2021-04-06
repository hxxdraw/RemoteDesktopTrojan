from modules import bot


def main():
    """
    Starting session
    """
    session = bot.RemoteDesktop()
    session.Activate()


if __name__ == "__main__":
    main()
