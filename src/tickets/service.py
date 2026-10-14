from tickets.schemas import Ticket, TicketResult


def classify_ticket(ticket: Ticket) -> TicketResult:
    text = ticket.message.lower()

    if "payment" in text or "invoice" in text:
        category = "billing"

    elif "login" in text or "error" in text:
        category = "technical"

    else:
        category = "general"

    priority = "high" if ticket.urgent else "normal"

    return TicketResult(
        category=category,
        priority=priority,
    )