"""
This file contains the tests for the Hotel class.
"""

import unittest
import os
from src.customer import Customer, CUSTOMERS


class TestCustomer(unittest.TestCase):
    """
    A class to represent the tests for the Hotel class.
    """

    def setUp(self):
        """
        Setup method to create a hotel object for testing.
        """
        # Create a customer object
        self.customer = Customer("Customer ABC", "This is a test customer")

    def test_customer_creation(self):
        """
        Test the creation of a Hotel.
        """
        self.assertTrue(isinstance(self.customer, Customer))

    def test_customer_display_information(self):
        """
        Test the display_information method of the Customer class.
        """

        # Call the display_information method
        _, name, info = self.customer.display_information()

        self.assertEqual(name, "Customer ABC")
        self.assertEqual(info, "This is a test customer")

    def test_customer_modify_information(self):
        """
        Test the modify_information method of the Customer class.
        """

        # Call the modify_information method
        self.customer.modify_information(
            "New Customer Name", "Updated information")

        # Call the display_information method
        _, name, info = self.customer.display_information()

        self.assertEqual(name, "New Customer Name")
        self.assertEqual(info, "Updated information")

    def test_customer_delete_customer(self):
        """
        Test the delete_hotel method of the Hotel class.
        """

        # Call the delete_hotel method
        self.customer.delete_customer()

        self.assertNotIn(self.customer, CUSTOMERS.customers)

    def test_customer_save_customers(self):
        """
        Test the save_customers method of the CustomerPersistentStorage class.
        """

        customer = Customer("Customer ABC", "This is a test customer")
        CUSTOMERS.save_customers()
        self.assertIn(customer, CUSTOMERS.customers)

    def test_customers_file_created(self):
        """
        Test if the customers_information.txt file is created.
        """

        CUSTOMERS.save_customers()

        self.assertTrue(os.path.exists("data/customers_information.txt"))

    def test_customers_add_customer(self):
        """
        Test the add_customer method of the CustomerPersistentStorage class.
        """
        # Create a customer object
        c = Customer("Customer ABC", "This is a test customer")
        CUSTOMERS.add_customer(c)
        self.assertIn(c, CUSTOMERS.customers)

    def tests_customers_get_customer_by_id(self):
        """
        Test the get_customer_by_id method of
        the CustomerPersistentStorage class.
        """
        # Create a customer object
        c = Customer("Customer ABC", "This is a test customer")
        CUSTOMERS.add_customer(c)
        customer = CUSTOMERS.get_customer_by_id(c.customer_id)
        self.assertEqual(customer, c)


# Run the tests
if __name__ == '__main__':
    unittest.main()
