from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self, protection: int = 120, price: float = 15.0):
        super().__init__(protection, price)

    def increase_price(self):
        self.price *= 1.20
