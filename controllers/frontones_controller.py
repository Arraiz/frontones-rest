import json
from models.fronton import Fronton
from config.config import TEST_DATA
from typing import List

TEST_PATH = "/test-data/fronton-coords.json"


class FrontonesController:

    def __init__(self):
        pass
    ##def dump_frontones_to_JSON():
        
    
    def get_frontones_from_JSON(self) -> List[Fronton]:
        """Return all the frontones to python list of fronton object

        """
        with open(TEST_DATA, 'r') as coords:
            data=coords.read()

        datajson = json.loads(data)
        coords.close()

        frontones = [Fronton(
            data["title"],
            data["lat"],
            data["lon"],
            data["index"],
            data["desc"],
            data["status"]) for data in datajson]
        
        coords.close()

        return frontones

