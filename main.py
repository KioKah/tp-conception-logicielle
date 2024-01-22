from datetime import datetime
from zoneinfo import ZoneInfo

maintenant = datetime.now()
heure_formatee = maintenant.strftime("%H:%M:%S")
print("Heure locale :", heure_formatee)

reunion = datetime.now(tz=ZoneInfo("Indian/Reunion"))
heure_formatee_reunion = reunion.strftime("%H:%M:%S")
print("Indian/Reunion --", heure_formatee_reunion)

paris = datetime.now(tz=ZoneInfo("Europe/Paris"))
heure_formatee_paris = paris.strftime("%H:%M:%S")
print("Europe/Paris --", heure_formatee_paris)
