from extensions import db
from helpers import CRUDMixin


class Order(db.Model, CRUDMixin):
    __tablename__ = 'order'

    intent = db.Column(db.String(16), nullable=False)
    order_type = db.Column(db.String(16), nullable=False)
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())
    
    def __init__(self, intent: str, order_type: str, price: float, quantity: int):
        self.intent = intent
        self.order_type = order_type
        self.price = price
        self.quantity = quantity
        
    def __repr__(self):
        return f"Order ID = {self.id}"