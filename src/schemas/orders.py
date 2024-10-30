from marshmallow import Schema, fields


class OrderSchema(Schema):
    id = fields.Int(required=True)
    order_type = fields.String(required=True)
    intent = fields.String(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)


order_schema = OrderSchema()