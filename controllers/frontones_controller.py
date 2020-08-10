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
            json.dump(frontones_dict, outfile, sort_keys=True, indent=4)
        outfile.close()
    
    def write_fronton_status_to_json(self, index, status:str,user:str) -> int:

        all_frontones = self.get_frontones_from_JSON()
        all_frontones[int(index)].set_fronton_status(status,user)
        self.write_frontones_to_json(all_frontones)
    

    def free_fronton_and_write_to_json(self,index,user):
        """
        
        """
        fronton = self.get_frontones_from_JSON()[int(index)]
        if fronton.get_fronton_user() == user:
            self.write_fronton_status_to_json(index,str(0),'None')
            return 1
        else:
            return 2


    def check_pick_and_write_fronton_to_json(self,lat,lon,index,user):

        """
        check for reservation and if so write to database, return a bolean 
        1: valid reservation
        2: not valod coordinates
        3: already taken
        4: other error
        """

        fronton = self.get_frontones_from_JSON()[int(index)]
        if fronton.get_fronton_status() == '0' and 'latloncheck' == 'latloncheck':
            self.write_fronton_status_to_json(index,str(1),user)
            return "1"
        else:
            if fronton.get_fronton_status() == '1':
                return "3"
            
            elif 'latloncheck' == 'latloncheck':
                return "2"

"""     # esto es una movida, hay que saber qioen lo reservo
    def release_and_write_fronton_to_json(self,lat,lon,index):
        if 'latloncheck' == 'latloncheck':
            self.write_fronton_status_to_json(index,str(1))
            print("write %s"% 1)
        else: 
            return 'not allowed to get this fronton' """




