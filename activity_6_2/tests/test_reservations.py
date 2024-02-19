"""
This file contains the tests for the Reservations class.
"""

import unittest
import os
from src.reservation import Reservation, RESERVATIONS
from src.hotel import Hotel
from src.customer import Customer


class TestReservations(unittest.TestCase):
    """
    A class to represent the tests for the Reservations class.
    """

    def setUp(self):
        """
        Setup method to create a reservation object for testing.
        """
        # Create a hotel object
        self.hotel = Hotel("Hotel ABC", "This is a test hotel")
        # Create a customer object
        self.customer = Customer("Customer ABC", "This is a test customer")
        # Create a reservation object
        self.reservation = Reservation(self.customer, self.hotel)

    def test_reservation_creation(self):
        """
        Test the creation of a reservation.
        """
        self.assertTrue(isinstance(self.reservation, Reservation))

    def test_reservation_display_information(self):
        """
        Test the display_information method of the Reservation class.
        """

        # Call the display_information method
        _, customer, hotel = self.reservation.display_information()

        self.assertEqual(customer, self.customer)
        self.assertEqual(hotel, self.hotel)

    def test_reservation_delete_hotel(self):
        """
        Test the delete_hotel method of the Reservation class.
        """

        # Call the delete_hotel method
        self.reservation.delete_reservation()

        self.assertNotIn(self.reservation, RESERVATIONS.reservations)

    def test_reservation_save_reservations(self):
        """
        Test the save_hotels method of the ReservationPersistentStorage class.
        """

        # Create a reservation object
        r = Reservation(self.customer, self.hotel)

        # Call the save_reservations method
        RESERVATIONS.save_reservations()

        self.assertTrue(r in RESERVATIONS.reservations)

    def test_reservations_file_created(self):
        """
        Test the save_reservations method of
        the ReservationsPersistentStorage class.
        """

        # Call the save_hotels method
        RESERVATIONS.save_reservations()

        self.assertTrue(os.path.exists(RESERVATIONS.path))

    def test_add_reservation(self):
        """
        Test the add_reservation method of the
        ReservationsPersistentStorage class.
        """
        # Create a hotel object
        r = Reservation(self.customer, self.hotel)
        RESERVATIONS.add_reservation(r)
        self.assertIn(r, RESERVATIONS.reservations)

    def test_get_reservation_by_id(self):
        """
        Test the get_reservation_by_id method of the
        HotelPersistentStorage class.
        """

        # Create a hotel object
        r = Reservation(self.customer, self.hotel)
        RESERVATIONS.add_reservation(r)

        # Call the get_reservation_by_id method
        reservation = RESERVATIONS.get_reservation_by_id(r.reservation_id)

        self.assertEqual(r, reservation)

    def test_file_created(self):
        """
        Test the save_resevations method of the
        ReservationsPersistentStorage class.
        """

        # Remove the file
        os.remove(RESERVATIONS.path)

        # Call the save_reservations method
        RESERVATIONS.save_reservations()

        self.assertTrue(os.path.exists(RESERVATIONS.path))


# Run the tests
if __name__ == '__main__':
    unittest.main()
