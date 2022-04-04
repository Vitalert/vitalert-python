from typing import List
import requests
import vitalert.settings as st


class Alert:

    def __init__(self, data) -> None:
        self.url: str = data["url"]
        self.lastItems: List[int] = data["lastItems"]
        self.id: str = data["id"]

        try:
            self.synced = data["synced"]
        except:
            pass


    def update_last_items(self, items: list):

        try:
            query = "mutation MyMutation {updateAlert(input: {id: \"%s\", lastItems: %s}){id}}" % (self.id, items)
            update = requests.post(st.API_URL, headers=st.API_HEADERS, json={"query": query})
            update.raise_for_status()

        except requests.exceptions.HTTPError as err:
            print(f"There was an error updating Last Items from Url {self.id}\nerror: {err}")
