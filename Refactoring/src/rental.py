class Rental:

    def __init__(self, movie, dayRented):
        self.__movie = movie
        self.__daysRented = dayRented

    def get_movie(self):
        return self.__movie

    def get_days_rented(self):
        return self.__daysRented

    def get_frequent_renter_points(self):
        return self.__movie.get_frequent_renter_points(self.__daysRented)

    def get_charge(self):
        return self.__movie.get_charge(self.__daysRented)
