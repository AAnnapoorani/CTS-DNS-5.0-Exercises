class CustomerRepository:
    def find_customer_by_id(self, customer_id):
        print("Customer Found :", customer_id)


class CustomerService:
    def __init__(self, repository):
        self.repository = repository
    def get_customer(self, customer_id):
        self.repository.find_customer_by_id(customer_id)

repository = CustomerRepository()
service = CustomerService(repository)
service.get_customer(101)