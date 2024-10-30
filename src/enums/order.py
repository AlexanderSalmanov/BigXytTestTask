from . import AutoEnum
from enum import auto


class OrderType(AutoEnum):
    ADD = auto()
    REMOVE = auto()

    
class OrderIntent(AutoEnum):
    BUY = auto()
    SELL = auto()