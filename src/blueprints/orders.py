from flask import Blueprint, request

from models.orders import Order
from enums.order import OrderIntent
from schemas.orders import order_schema
from helpers import to_error_response, to_success_response
import constants


bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    try:
        Order.create(**data)
    except TypeError:
        return to_error_response(constants.INVALID_INPUT_DATA)
    
    suggestions = {
        'best_sell': order_schema.dump(
            Order.query.filter_by(intent=OrderIntent.SELL.value)
            .order_by('price')
            .all(), 
            many=True
        ),
        'best_buy': order_schema.dump(
            Order.query.filter_by(intent=OrderIntent.BUY.value)
            .order_by('price')
            .all(), 
            many=True
        )
    }
    return to_success_response(suggestions, status_code=201)


@bp.route('/delete/<int:order_id>', methods=['DELETE'])
def delete(order_id: int):
    if not (order_obj := Order.get_by_id(order_id)):
        return to_error_response(constants.INSTANCE_NOT_FOUND(Order.__tablename__, order_id))
    
    order_obj.delete()
    return to_success_response(status_code=204)


@bp.route('/get-all', methods=['GET'])
def get_all():
    return to_success_response(order_schema.dump(Order.query.all(), many=True))