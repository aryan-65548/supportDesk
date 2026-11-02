from app.schemas.ticket import TicketCreate, TicketStatus

_tickets: dict[int, dict] = {}
_next_id = 1


def create_ticket(data: TicketCreate) -> dict:
    global _next_id
    ticket = {
        "id": _next_id,
        **data.model_dump(),
        "status": TicketStatus.open,
    }
    _tickets[_next_id] = ticket
    _next_id += 1
    return ticket


def list_tickets(status: TicketStatus | None = None, limit: int = 10) -> list[dict]:
    tickets = list(_tickets.values())
    if status is not None:
        tickets = [t for t in tickets if t["status"] == status]
    return tickets[:limit]


def get_ticket(ticket_id: int) -> dict | None:
    return _tickets.get(ticket_id)


def update_status(ticket_id: int, status: TicketStatus) -> dict | None:
    ticket = _tickets.get(ticket_id)
    if ticket is not None:
        ticket["status"] = status
    return ticket