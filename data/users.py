"""
<Description>
    Remote desktop database control file
    It uses for user operations
    Using sqlite3 database >> (.db)
"""

import sqlite3
import data.settings


class UserInfo(object):

    # Admin data
    admin_id = 0    # telegram id
    admin_username = "username"  # displayed name

    def __init__(self):
        """
        Saving data if not exists
        """

        # Connecting to database (if not exists > creating)
        try:
            self.connection = sqlite3.connect(f'{data.settings.db_path}\\UserData.db')
        except:
            exit()

        # Creating control <cursor>
        self.cursor = self.connection.cursor()

        # default patterns
        self.insert_command = "Insert into users Values(?, ?);"    # (<?> = value, <?> = value)
        self.get_command = "Select * from Users;"
        self.delete_command = "Delete From Users where user_id=?;"

        # Creating table if not exists then receiving all values
        self.cursor.execute("Create table if not exists Users(user_id INT, username TEXT);")

        # trying to find main user in table
        self.cursor.execute("Select * from Users where user_id = ?;", (self.admin_id,))

        # if output is clear, adding main user >> admin
        if not self.cursor.fetchall():
            self.cursor.execute(self.insert_command, (self.admin_id, self.admin_username))

        self.connection.commit()    # saving changes

    def newUser(self, user_id, username):
        """
        Adding new user by id and username
        :param user_id: int
        :param username: str
        :return:
        """
        self.cursor.execute(self.insert_command, (user_id, username))   # adding new user <id, name>
        self.connection.commit()    # saving changes
        self.connection.close()     # closing connection
        return f'{username} ({user_id}) was added.'

    def delUser(self, target_id):
        """
        Deleting user by id
        :return:
        """
        try:
            self.cursor.execute(self.delete_command, (target_id, ))
            self.connection.commit()
            self.connection.close()
            return f'"{target_id}" was removed.'
        except Exception as e:
            return e

    def getUsers(self):
        """
        This function returns all activated users
        :return: string
        """
        self.cursor.execute(self.get_command)
        users = {user_id: username for user_id, username in self.cursor.fetchall()}
        self.connection.close()     # closing connection
        return users

    def isValid(self, user_id):
        """
        This function checks user id validity
        :param user_id:
        :return: bool
        """
        # loading data from table <Users>
        self.cursor.execute(self.get_command)
        for id, username in self.cursor.fetchall():
            if user_id == id:
                self.connection.close()
                # if user_id is valid
                return True

        # if user id is not found
        return False

