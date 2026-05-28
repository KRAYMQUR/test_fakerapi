from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel): 
    id : int
    title : str
    description : str 
    pageCount : int
    excerpt : str 
    publishDate : datetime 