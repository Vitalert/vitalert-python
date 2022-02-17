from vitalert import Vitalert

v = Vitalert()
a = v.users.getProUsers()

user = a[0]
user.getAlerts()
print(alert.url for alert in user.alerts.alerts )
