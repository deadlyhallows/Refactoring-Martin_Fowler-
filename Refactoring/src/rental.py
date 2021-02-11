from Refactoring.src.movie import Movie


class Rental:

    def __init__(self, movie, dayRented):
        self.__movie = movie
        self.__daysRented = dayRented

    def get_movie(self):
        return self.__movie

    def get_days_rented(self):
        return self.__daysRented

    def get_charge(self):
        price_code = self.get_movie().price_code
        days_rented = self.get_days_rented()
        thisAmount = 0
        if price_code == Movie.REGULAR:
            thisAmount += 2
            if days_rented > 2:
                thisAmount += (days_rented - 2) * 1.5
        if price_code == Movie.NEW_RELEASE:
            thisAmount += days_rented * 3
        if price_code == Movie.CHILDREN:
            thisAmount += 1.5
            if days_rented > 3:
                thisAmount += (days_rented - 3) * 1.5

        return thisAmount
