from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import logging

logging.basicConfig(filename="traitement.log", encoding="utf-8", level=logging.DEBUG)


def afficher_heure(time_zone: str):
    if time_zone is None:
        logging.error("Aucune timezone n'a été renseignée")
        raise ValueError("Aucune timezone n'a été renseignée")
    logging.debug(f"Demande d'heure sur le timezone : {time_zone}")
    try:
        maintenant = datetime.now(tz=ZoneInfo(time_zone))
        heure_formatee = maintenant.strftime("%H:%M:%S")
    except ZoneInfoNotFoundError as e:
        logging.error(f"Erreur : {e}")
        raise e
    else:
        print(f"Heure dans la zone {time_zone} : {heure_formatee}")


logging.info(f"Lancement du traitement")

afficher_heure("Indian/Reunion")
afficher_heure("Europe/Paris")
afficher_heure("??")
