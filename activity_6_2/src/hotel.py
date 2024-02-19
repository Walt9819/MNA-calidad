"""
This module contains the hotel class and the persistent storage class.
"""

from src.utilities import check_file_existence, get_values


class Hotel:
    """
    A class to represent a hotel.
    """
    def __init__(self, name, information, hotel_id=None):
        self.name = name
        self.information = information
        # If have an ID, use it, otherwise add a new hotel
        if hotel_id is not None:
            self.hotel_id = hotel_id
        else:
            HOTELS.add_hotel(self)

    def display_information(self):
        """
        Display the hotel information.
        """
        if self.hotel_id:
            print(f"Hotel ID: {self.hotel_id}")
        print(f"Hotel Name: {self.name}")
        print(f"Information: {self.information}")
        return self.hotel_id, self.name, self.information

    def modify_information(self, name, information):
        """
        Modify the hotel information.
        """
        self.name = name
        self.information = information

    def delete_hotel(self):
        """
        Delete the hotel from the database.
        """
        HOTELS.hotels.remove(self)
        HOTELS.save_hotels()


class HotelPersistentStorage:
    """
    A class to represent the persistent storage of the application.
    """
    def __init__(self):
        self.hotels = []
        self.path = "data/hotels_information.txt"

    def save_hotels(self):
        """
        Save hotels information to the database (text file)
        """
        with open(self.path, "w", encoding='utf-8') as file:
            for hot in self.hotels:
                file.write(f"{hot.hotel_id},{hot.name},{hot.information}\n")

    def get_hotel_by_id(self, hotel_id):
        """
        Get a hotel by its ID.
        """
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                return hotel
        return None

    def get_hotels(self):
        """
        Retrieve hotels information from the database (text file)
        """
        if not check_file_existence(self.path):
            return None
        with open(self.path, "r", encoding='utf-8') as file:
            for i, line in enumerate(file):
                v = get_values(i, line)
                if v is not None:
                    h_id, name, information = v
                    self.hotels.append(Hotel(name, information, hotel_id=h_id))
        return self.hotels

    def add_hotel(self, hotel):
        """
        Add a hotel to the database.
        """
        new_id = len(self.hotels) + 1
        self.hotels.append(hotel)
        # Set the hotel_id
        hotel.hotel_id = new_id
        self.save_hotels()
        return hotel


HOTELS = HotelPersistentStorage()
HOTELS.get_hotels()
