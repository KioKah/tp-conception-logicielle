from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import logging
import sys


def get_fichier_sortie_args():
    print(sys.argv)
    if len(sys.argv) > 1:
        return sys.argv[1]
    return None


def get_fichier_sortie_env():
    from dotenv import load_dotenv
    import os

    load_dotenv()
    if os.environ.get("LOG_FILE") is not None:
        return os.environ["LOG_FILE"]
    return None


def get_fichier_sortie():
    return get_fichier_sortie_args() or get_fichier_sortie_env() or "traitement.log"


logging.basicConfig(
    filename=get_fichier_sortie(), encoding="utf-8", level=logging.DEBUG
)


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
