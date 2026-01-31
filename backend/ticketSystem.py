

from dataclasses import dataclass
import queue
import uuid


@dataclass
class PurchaseRequest:
    user_id: str
    request_id: str
    event_id: str
    quantity: int


class TicketSystem:
    def __init__(self):
        self._purchase_queue = queue.Queue(maxsize=1000)

    def purchase_tickets(self, user_id: str, event_id: str, quantity: int) -> None:
        request = PurchaseRequest(user_id, uuid.uuid4(), event_id, quantity)

        try:
            self._purchase_queue.put(request, timeout=0.1)
        except queue.Full:
            raise RuntimeError("Queue is full. Try again later")

    def purchase_workers(self) -> None:
        while True:
            request = self._purchase_queue.get()
            self.process_purchase(request)

    def process_purchase(self, request: PurchaseRequest):
        pass

