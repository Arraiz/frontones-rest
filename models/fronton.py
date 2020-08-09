import json
class Fronton:
    def __init__(self,title,lat,lon,index,desc,status):
        self.title = title
        self.lat = lat
        self.lon = lon
        self.index = index
        self.desc = desc
        self.status = status

    
    def get_fronton(self):
        return [ {"lat":str(self.lat)},
                 {"lon":str(self.lon)},
                 {"index":str(self.index)},
                 {"desc":str(self.desc)}]


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def as_dict(self):
        return {"lat":str(self.lat), "lon":str(self.lon), "index":str(self.index),"desc":str(self.desc)}

    def set_fronton_status(self,status:int):
        self.status=status

    
