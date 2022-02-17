import requests
from typing import List
import vitalert.settings as st
from vitalert.alerts.alert import Alert


class Alerts:

    def __init__(self, userId) -> None:
        self.userId = userId
        self.alerts = []

    def getAlerts(self) -> List[Alert]:
        query = "query MyQuery { listAlertsAdmin(filter: {userId: {eq: \"%s\"}}) {items {url lastItems id}}}" % (self.userId)

        alerts = requests.post(st.API_URL, headers=st.API_HEADERS, json={"query": query}).json()

        alerts = alerts["data"]["listAlertsAdmin"]["items"]
        self.alerts = [Alert(data) for data in alerts]
        return self.alerts
