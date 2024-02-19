"""
This module contains the customer class and the persistent storage class.
"""

from src.utilities import check_file_existence, get_values


class Customer:
    """
    A class to represent a customer.
    """
    def __init__(self, name, information, customer_id=None):
        self.name = name
        self.information = information
        # If have an ID, use it, otherwise add a new hotel
        if customer_id is not None:
            self.customer_id = customer_id
        else:
            CUSTOMERS.add_customer(self)

    def display_information(self):
        """
        Display the customer information.
        """
        if self.customer_id:
            print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.name}")
        print(f"Information: {self.information}")
        return self.customer_id, self.name, self.information

    def modify_information(self, name, information):
        """
        Modify the customer information.
        """
        self.name = name
        self.information = information

    def delete_customer(self):
        """
        Delete the customer from the database.
        """
        CUSTOMERS.customers.remove(self)
        CUSTOMERS.save_customers()


class CustomerPersistentStorage:
    """
    A class to represent the persistent storage of the application.
    """
    def __init__(self):
        self.customers = []
        self.path = "data/customers_information.txt"

    def save_customers(self):
        """
        Save customers information to the database (text file)
        """
        with open(self.path, "w", encoding='utf-8') as file:
            for cust in self.customers:
                line = f"{cust.customer_id},{cust.name},"
                line += f"{cust.information}\n"
                file.write(line)

    def get_customer_by_id(self, customer_id):
        """
        Get a customer by its ID.
        """
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def add_customer(self, customer):
        """
        Add a customer to the database.
        """
        new_id = len(self.customers) + 1
        self.customers.append(customer)
        # Set the customer_id
        customer.customer_id = new_id
        self.save_customers()
        return customer

    def get_customers(self):
        """
        Retrieve customers information from the database (text file)
        """
        # Find the file and check if it exists
        if not check_file_existence(self.path):
            return None
        # All lines must be read
        with open(self.path, "r", encoding='utf-8') as file:
            for i, line in enumerate(file):
                v = get_values(i, line)
                if v is not None:
                    c_id, name, information = v
                    self.customers.append(
                        Customer(name, information, customer_id=c_id))
        return self.customers


CUSTOMERS = CustomerPersistentStorage()
CUSTOMERS.get_customers()
