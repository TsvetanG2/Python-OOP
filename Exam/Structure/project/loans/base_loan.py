class BaseLoan:
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    def increase_interest_rate(self):
        self.interest_rate += 0.5
        return self.interest_rate


