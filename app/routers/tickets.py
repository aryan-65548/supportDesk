from fastapi import APIRouter, HTTPException, Query

from app.schemas.ticket import TicketCreate, TicketRead, TicketStatus, TicketUpdate
from app.services import ticket_service

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.post("", response_model=TicketRead, status_code=201)
def create_ticket(payload: TicketCreate):
    return ticket_service.create_ticket(payload)

@router.get("", response_model=list[TicketRead])
def list_tickets(
    status: TicketStatus | None = None,
    limit: int = Query(default=10, ge=1, le=100),
):
    return ticket_service.list_tickets(status=status, limit=limit)

@router.get("/{ticket_id}", response_model=TicketRead)
def get_ticket(ticket_id: int):
    ticket = ticket_service.get_ticket(ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.patch("/{ticket_id}", response_model=TicketRead)
def update_ticket_status(ticket_id: int, payload: TicketUpdate):
    ticket = ticket_service.update_status(ticket_id, payload.status)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket