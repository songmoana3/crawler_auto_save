# datetime chk, db_value_chk
from dataclasses import dataclass

@dataclass
class Datetime:
    
    datetime:str
    
    def __init__(self,datetime):
        if len(datetime) != 8:
            raise ValueError ("[HINT]:: Date time length must be 6. Format : 20220601")

        if type(datetime) != str:
            raise ValueError ("[HINT]:: Date time must be string. Format : 20220601")
        