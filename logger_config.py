import logging
import sys

logger = logging.getLogger('Weather')
logging.basicConfig(
        filename="weather.log",
        filemode="w",
        format="[%(asctime)s] %(levelname).1s %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level= logging.INFO
    )
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname).1s %(message)s"))
logger.addHandler(handler)