"""
This file contains the tests for the Hotel class.
"""

import unittest
import os
from src.hotel import Hotel, HOTELS


class TestHotel(unittest.TestCase):
    """
    A class to represent the tests for the Hotel class.
    """

    def setUp(self):
        """
        Setup method to create a hotel object for testing.
        """
        # Create a hotel object
        self.hotel = Hotel("Hotel ABC", "This is a test hotel")

    def test_hotel_creation(self):
        """
        Test the creation of a Hotel.
        """
        self.assertTrue(isinstance(self.hotel, Hotel))

    def test_hotel_display_information(self):
        """
        Test the display_information method of the Hotel class.
        """

        # Call the display_information method
        _, name, info = self.hotel.display_information()

        self.assertEqual(name, "Hotel ABC")
        self.assertEqual(info, "This is a test hotel")

    def test_hotel_modify_information(self):
        """
        Test the modify_information method of the Hotel class.
        """

        # Call the modify_information method
        self.hotel.modify_information("New Hotel Name", "Updated information")

        # Call the display_information method
        _, name, info = self.hotel.display_information()

        self.assertEqual(name, "New Hotel Name")
        self.assertEqual(info, "Updated information")

    def test_hotel_delete_hotel(self):
        """
        Test the delete_hotel method of the Hotel class.
        """

        # Call the delete_hotel method
        self.hotel.delete_hotel()

        self.assertNotIn(self.hotel, HOTELS.hotels)

    def test_hotels_save_hotels(self):
        """
        Test the save_hotels method of the HotelPersistentStorage class.
        """

        # Create a hotel object
        hotel = Hotel("Hotel ABC", "This is a test hotel")

        # Call the save_hotels method
        HOTELS.save_hotels()

        self.assertTrue(hotel in HOTELS.hotels)

    def test_hotels_file_created(self):
        """
        Test the save_hotels method of the HotelPersistentStorage class.
        """

        # Call the save_hotels method
        HOTELS.save_hotels()

        self.assertTrue(os.path.exists(HOTELS.path))

    def test_add_hotel(self):
        """
        Test the add_hotel method of the HotelPersistentStorage class.
        """
        # Create a hotel object
        h = Hotel("Hotel ABC", "This is a test hotel")
        HOTELS.add_hotel(h)
        self.assertIn(h, HOTELS.hotels)

    def test_get_hotel_by_id(self):
        """
        Test the get_hotel_by_id method of the HotelPersistentStorage class.
        """

        # Create a hotel object
        h = Hotel("Hotel ABC", "This is a test hotel")
        HOTELS.add_hotel(h)

        # Call the get_hotel_by_id method
        hotel = HOTELS.get_hotel_by_id(h.hotel_id)

        self.assertEqual(h, hotel)

    def test_file_created(self):
        """
        Test the save_hotels method of the HotelPersistentStorage class.
        """

        # Remove the file
        os.remove(HOTELS.path)

        # Call the save_hotels method
        HOTELS.save_hotels()

        self.assertTrue(os.path.exists(HOTELS.path))


# Run the tests
if __name__ == '__main__':
    unittest.main()
