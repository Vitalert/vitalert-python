import requests
from pyVinted import Vinted
from typing import List
import vitalert.settings as st
from vitalert.alerts.alerts import Alerts
from vitalert.alerts.alert import Alert



class User:
    """
    The User class represents a registred user on cognito and all of its known informations.
    """
    def __init__(self, data, group) -> None:
        self.userId: str = data["Username"]

        # TODO : find a way to retrieve email
        #self.email: str = data["Attributes"][2]["Value"]
        self.group: str = group
        self.rawData: dict = data
        self.useTelegram: bool = False
        self.telegramId: str = ""  # TODO retrieve user infos on appsync (not cognito)
        self.discordWebhook = ""
        self.complete_user()
        self.alerts = Alerts(data["Username"])
        self.alerts.getAlerts()


    def complete_user(self):
        query = "query MyQuery {listUsers(filter: {id: {eq: \"%s\"}}) {items {discordWebhook telegramId useTelegram}}}" % (self.userId)
        userInfos = requests.post(st.API_URL, headers=st.API_HEADERS, json={"query": query}).json()
        print(userInfos)
        userInfos = userInfos['data']['listUsers']["items"][0]

        #uses telegram ?
        useTelegram = userInfos["useTelegram"]
        if useTelegram is not None:
            self.useTelegram = useTelegram
        # telegram Id
        telegramId = userInfos["telegramId"]
        if telegramId is not None:
            self.telegramId = telegramId

        #Discord WebHook
        webhook = userInfos["discordWebhook"]
        if webhook is not None:
            self.discordWebhook = webhook

    def getAlerts(self) -> List[Alert]:
        return self.alerts.getAlerts()

    def listCurrentAlerts(self) -> List[Alert]:
        return self.alerts.alerts
        