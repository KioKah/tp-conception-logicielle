from datetime import datetime

maintenant = datetime.now()
heure_formatee = maintenant.strftime("%H:%M:%S")
print(heure_formatee)