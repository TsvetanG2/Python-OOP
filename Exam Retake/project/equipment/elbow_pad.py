from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self, protection: int = 90, price: float = 25.0):
        super().__init__(protection, price)

    def increase_price(self):
        self.price *= 1.10


