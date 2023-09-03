class BaseClient:
    def __init__(self, name, client_id, income):
        if not name.strip():
            raise ValueError("Client name cannot be empty!")

        if len(client_id) != 10:
            raise ValueError("Client ID should be 10 symbols long!")

        if income <= 0.0:
            raise ValueError("Income must be greater than zero!")

        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = 0.0
        self.loans = []

    def __str__(self):
        return f"Client: {self.name}, ID: {self.client_id}, Income: {self.income}, Loans: {len(self.loans)}"


class PersonalClient(BaseClient):
    def increase_clients_interest(self):
        # Implement interest increase logic for personal clients
        self.interest += 0.1


class BusinessClient(BaseClient):
    def increase_clients_interest(self):
        # Implement interest increase logic for business clients
        self.interest += 0.2