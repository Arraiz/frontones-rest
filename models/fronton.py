import json
from typing import List
class Fronton:
    def __init__(self,title,lat,lon,index,desc,status=0,user='None'):
        self.title = title
        self.lat = lat
        self.lon = lon
        self.index = index
        self.desc = desc
        self.status = status
        self.user = user

    
    def get_fronton(self):
        return [{"title":str(self.title)},
                {"lat":str(self.lat)},
                {"lon":str(self.lon)},
                {"index":str(self.index)},
                {"desc":str(self.desc)},
                {"status":str(self.status)},
                {"user":str(self.user)}]


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def get_fronton_user(self):
        return self.user

    def get_fronton_status(self):
        return self.status

    def as_dict(self):
        return {"title":str(self.title),"lat":str(self.lat), "lon":str(self.lon), "index":str(self.index),"desc":str(self.desc),"status":str(self.status),"user":str(self.user)}

    def set_fronton_status(self,status,user):
        self.status=status
        self.user=user

    
