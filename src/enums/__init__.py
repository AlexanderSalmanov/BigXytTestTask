from enum import Enum


class AutoEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()
    
    @classmethod
    def get_choice_pair_values(cls):
        return [(item.value, item.name) for item in cls]