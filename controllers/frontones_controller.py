import json
from models.fronton import Fronton
from config.config import TEST_DATA
from typing import List

TEST_PATH = "test-data/fronton-coords.json"


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
            data["status"],
            data["user"]) for data in datajson]
        
        coords.close()

        return frontones

    def write_frontones_to_json(self, frontones: List[Fronton]):
        frontones_dict=[fronton.__dict__ for fronton in frontones]
        with open(TEST_DATA, 'w') as outfile:
            json.dump(frontones_dict, outfile)
        outfile.close()
    
    def write_fronton_status_to_json(self, index, status:str,user:str):
        all_frontones = self.get_frontones_from_JSON()
        all_frontones[int(index)].set_fronton_status(status,user)
        self.write_frontones_to_json(all_frontones)
    

    def check_pick_and_write_fronton_to_json(self,lat,lon,index,user):
        if 'latloncheck' == 'latloncheck':
            self.write_fronton_status_to_json(index,str(1),user)
            print("write %s"% 1)
        else: 
            return 'not allowed to get this fronton'

"""     # esto es una movida, hay que saber qioen lo reservo
    def release_and_write_fronton_to_json(self,lat,lon,index):
        if 'latloncheck' == 'latloncheck':
            self.write_fronton_status_to_json(index,str(1))
            print("write %s"% 1)
        else: 
            return 'not allowed to get this fronton' """




