"""
Represent and save reservations information to the database.
"""

from src.hotel import HOTELS
from src.customer import CUSTOMERS
from src.utilities import check_file_existence, get_values


class Reservation:
    """
    A class to represent a reservation.
    """
    def __init__(self, customer, hotel, reservation_id=None):
        self.customer = customer
        self.hotel = hotel
        # If have an ID, use it, otherwise add a new reservation
        if reservation_id is not None:
            self.reservation_id = reservation_id
        else:
            RESERVATIONS.add_reservation(self)

    def display_information(self):
        """
        Display the reservation information.
        """
        if self.reservation_id:
            print(f"Reservation ID: {self.reservation_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Hotel: {self.hotel.name}")
        return self.reservation_id, self.customer, self.hotel

    def delete_reservation(self):
        """
        Delete the reservation from the database.
        """
        RESERVATIONS.reservations.remove(self)
        RESERVATIONS.save_reservations()


class ReservationPersistentStorage:
    """
    A class to represent the persistent storage of the application.
    """
    def __init__(self):
        self.reservations = []
        self.path = "data/reservations_information.txt"

    def save_reservations(self):
        """
        Save reservations information to the database (text file)
        """
        with open(self.path, "w", encoding='utf-8') as file:
            for res in self.reservations:
                line = f"{res.reservation_id},{res.customer.customer_id},"
                line += f"{res.hotel.hotel_id}\n"
                file.write(line)

    def get_reservations(self):
        """
        Retrieve reservations information from the database (text file)
        """
        # Check the file existence
        if not check_file_existence(self.path):
            return None
        # Read the file if exists and get the reservations
        with open(self.path, "r", encoding='utf-8') as file:
            for i, line in enumerate(file):
                reservation_id, customer_id, hotel_id = get_values(i, line)
                customer = CUSTOMERS.get_customer_by_id(customer_id)
                hotel = HOTELS.get_hotel_by_id(hotel_id)
                self.reservations.append(
                    Reservation(customer, hotel, reservation_id=reservation_id)
                    )
        return self.reservations

    def get_reservation_by_id(self, reservation_id):
        """
        Get a reservation by its ID.
        """
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                return reservation
        return None

    def add_reservation(self, reservation):
        """
        Add a reservation to the database.
        """
        new_id = len(self.reservations) + 1
        self.reservations.append(reservation)
        # Set the reservation_id
        reservation.reservation_id = new_id
        self.save_reservations()
        return reservation


RESERVATIONS = ReservationPersistentStorage()
RESERVATIONS.get_reservations()
