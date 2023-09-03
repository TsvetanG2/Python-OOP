from clients.student import Student
from clients.adult import Adult
from loans.mortgage_loan import MortgageLoan
from loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in ["StudentLoan", "MortgageLoan"]:
            raise Exception("Invalid loan type!")

        if loan_type == "StudentLoan":
            loan = StudentLoan()
        elif loan_type == "MortgageLoan":
            loan = MortgageLoan()

        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in ["Student", "Adult"]:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        if any(client.client_id == client_id for client in self.clients):
            return "Client ID already exists."

        if client_type == "Student":
            client = Student(client_name, client_id, income)
        elif client_type == "Adult":
            client = Adult(client_name, client_id, income)

        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        client = next((client for client in self.clients if client.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")

        loan = next((loan for loan in self.loans if isinstance(loan, StudentLoan if loan_type == "StudentLoan" else MortgageLoan)), None)
        if not loan:
            raise Exception("Invalid loan type!")

        if isinstance(client, Student) and not isinstance(loan, StudentLoan):
            raise Exception("Inappropriate loan type!")

        if isinstance(client, Adult) and not isinstance(loan, MortgageLoan):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)  # Remove the loan before granting
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        client = next((client for client in self.clients if client.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        changed_loans = [loan for loan in self.loans if isinstance(loan, StudentLoan if loan_type == "StudentLoan" else MortgageLoan)]
        for loan in changed_loans:
            loan.increase_interest_rate()
        return f"Successfully changed {len(changed_loans)} loans."

    def increase_clients_interest(self, min_rate):
        changed_clients = [client for client in self.clients if client.interest < min_rate]
        for client in changed_clients:
            client.increase_clients_interest()
        return f"Number of clients affected: {len(changed_clients)}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)
        loans_count_granted_to_clients = sum(len(client.loans) for client in self.clients)
        granted_sum = sum(loan.amount for client in self.clients for loan in client.loans)
        loans_count_not_granted = len(self.loans) - loans_count_granted_to_clients
        not_granted_sum = sum(loan.amount for loan in self.loans if loan not in [loan for client in self.clients for loan in client.loans])
        avg_client_interest_rate = sum(client.interest for client in self.clients) / total_clients_count if total_clients_count > 0 else 0

        return f"Active Clients: {total_clients_count}\nTotal Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {loans_count_not_granted + 3}, Total Sum: {not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

bank = BankApp(3)
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))
print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.remove_client('1234567999'))
print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))
print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))
print(bank.get_statistics())
