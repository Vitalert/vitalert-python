from pyVinted.items.item import Item
from vitalert.users.user import User
from typing import List
import requests

class Notifier:
    def __init__(self) -> None:
        pass

    def sendTelegram(self, items: List[Item], user: User):
        if items != [] and items != None:
            for item in items:
                message = f"{item.title}\nPrice: {item.price}{item.currency}\n\nURL: {item.url}"
                requests.get(
                    f"https://api.telegram.org/bot2064361445:AAEdNxt_fWtXgWeLs_En_PyzqQSUrNtcHxI/sendMessage?text={message}&chat_id={user.telegramId}")

    def sendDiscord(self, items: List[Item], user: User):
        message = {
            "username": "Vitalert",
            "avatar_url": "",
            "content": "",
            "embeds": [
                {
                    "color": 10037693,
                    "timestamp": "",
                    "url": "https://www.vinted.fr/hommes/vetements/vetements-de-sport-and-accessoires/accessoires-de-sports/montres-sport-and-bracelets-connectes/1510452151-smartwatch",
                    "author": {
                        "name": "HTRDCV",
                        "url": "https://www.vinted.fr/hommes/vetements/vetements-de-sport-and-accessoires/accessoires-de-sports/montres-sport-and-bracelets-connectes/1510452151-smartwatch",
                        "icon_url": "https://images1.vinted.net/t/02_0202a_uq6vCa75UbWx9wJC1Pw2nrWx/f800/1639561237.jpeg?s=5a7255bba7261b3a5c65f380656487b7ead131d1"
                    },
                    "image": {
                        "url": "https://images1.vinted.net/t/02_0202a_uq6vCa75UbWx9wJC1Pw2nrWx/f800/1639561237.jpeg?s=5a7255bba7261b3a5c65f380656487b7ead131d1"
                    },
                    "thumbnail": {},
                    "footer": {
                        "text": "Vitalert Demo"
                    },
                    "fields": [
                        {
                            "name": "Price:",
                            "value": "20€",
                            "inline": True
                        },
                        {
                            "name": "Condition:",
                            "value": "Très bon état",
                            "inline": True
                        },
                        {
                            "name": "Size:",
                            "value": "M",
                            "inline": True
                        }
                    ]
                },
                {
                    "title": "-------BUY-------",
                    "color": 0,
                    "timestamp": "",
                    "url": "https://www.vinted.fr/hommes/vetements/vetements-de-sport-and-accessoires/accessoires-de-sports/montres-sport-and-bracelets-connectes/1510452151-smartwatch",
                    "author": {},
                    "image": {},
                    "thumbnail": {},
                    "footer": {},
                    "fields": []
                }
            ],
            "components": [

      ]
        }

        if items != [] and items != None:
            for item in items:
                message["embeds"][0]["author"]["name"] = item.title
                message["embeds"][0]["author"]["url"] = f"{item.url}"
                message["embeds"][0]["author"]["icon_url"] = f"{item.photo}"
                message["embeds"][0]["fields"][0]["value"] = f"{item.price}{item.currency}"
                #message["embeds"][0]["fields"][0]["value"] = f"{item.url}"
                #message["embeds"][0]["fields"][1]["value"] = f"{item.status_id}"
                message["embeds"][0]["fields"][2]["value"] = f"{item.size_title}"
                message["embeds"][0]["image"]["url"] = f"{item.photo}"
                message["embeds"][1]["url"] = f"{item.url}"

                requests.post(user.discordWebhook, json=message)







notifier = Notifier()