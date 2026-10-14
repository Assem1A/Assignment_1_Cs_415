from fastapi import APIRouter

from tickets.schemas import Ticket, TicketResult
from tickets.service import classify_ticket


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


@router.post(
    "/classify",
    response_model=TicketResult,
)
def classify_ticket_endpoint(ticket: Ticket) -> TicketResult:
    return classify_ticket(ticket)