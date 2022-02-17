from vitalert.notifier import notifier
from vitalert.users.users import users
class Vitalert:
    def __init__(self) -> None:
        self.notifier = notifier
        self.users = users