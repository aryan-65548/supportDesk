from enum import Enum
from pydantic import BaseModel, Field

class TicketStatus(str, Enum):
    open="open"
    in_progress="in_progress"
    closed="closed"

class TicketCreate(BaseModel):
    title:str=Field(min_length=3, max_length=100)
    description: str

class TicketUpdate(BaseModel):
    status: TicketStatus 

class TicketRead(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus


