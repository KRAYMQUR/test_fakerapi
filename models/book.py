from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Book(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    pageCount: Optional[int] = None
    excerpt: Optional[str] = None
    publishDate: Optional[datetime] = None
