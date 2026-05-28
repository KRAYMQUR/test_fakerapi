from pydantic import BaseModel



class Author(BaseModel):
    id : int
    idBook : int 
    firstName : str 
    lastName : str