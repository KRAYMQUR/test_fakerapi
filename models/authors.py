from pydantic import BaseModel
from typing import Optional


class Author(BaseModel):
    id: int
    idBook: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
