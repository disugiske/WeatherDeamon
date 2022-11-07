import logging
import sys

logger = logging.getLogger('Weather')
logging.basicConfig(
        datefmt="%d-%b-%y %H:%M:%S",
        level= logging.INFO,
        stream=sys.stdout,
    )
handler = logging.FileHandler('weather.log', 'w', 'utf-8')
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname).1s %(message)s"))
logger.addHandler(handler)