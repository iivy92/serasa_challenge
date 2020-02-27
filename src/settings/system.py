import os

class SystemSettings():

    PATH_TRANSACTIONS = os.environ.get("PATH_TRANSACTIONS")

    def __init__(self):
        self.__validate_path()

    def __validate_path(self):
        if self.PATH_TRANSACTIONS is None:
            raise ValueError("PATH_TRANSACTIONS should not be empty")