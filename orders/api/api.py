import uuid
from datetime import datetime
from uuid import UUID

from starlette.responses import Response
from starlette import status

from orders.app import app

order = {
    "id": uuid.uuid4(),
    "status": "delivered",
    "created_at": datetime.utcnow(),
    "order": [
        {
            "product": "cappuccino",
            "size": "medium",
            "quantity": 1,
        },
    ],
}


@app.get("/orders")
def get_orders():
    return {"orders": [order]}


@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order():
    return order


@app.get("/orders/{id}")
def get_order(id: UUID):
    return order


@app.put("/orders/{id}")
def get_order(id: UUID):
    return order


@app.delete("/orders/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(id: UUID):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("/orders/{id}/cancel")
def cancel_order(id: UUID):
    return order


@app.post("/orders/{id}/pay")
def pay_order(id: UUID):
    return order
