from Refactoring.src.movie import Movie


class Rental:

    def __init__(self, movie, dayRented):
        self.__movie = movie
        self.__daysRented = dayRented

    def get_movie(self):
        return self.__movie

    def get_days_rented(self):
        return self.__daysRented

    def get_frequent_renter_points(self):

        if self.get_movie().price_code == Movie.NEW_RELEASE and self.get_days_rented() > 1:
            return 2
        else:
            return 1

    def get_charge(self):

        thisAmount = 0
        if self.get_movie().price_code == Movie.REGULAR:
            thisAmount += 2
            if self.get_days_rented() > 2:
                thisAmount += (self.get_days_rented() - 2) * 1.5
        if self.get_movie().price_code == Movie.NEW_RELEASE:
            thisAmount += self.get_days_rented() * 3
        if self.get_movie().price_code == Movie.CHILDREN:
            thisAmount += 1.5
            if self.get_days_rented() > 3:
                thisAmount += (self.get_days_rented() - 3) * 1.5

        return thisAmount
