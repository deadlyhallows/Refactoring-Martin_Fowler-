from Refactoring.src.movie import Movie


class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = list()

    def add_rental(self, rental):
        self.__rentals.append(rental)

    def get_statement(self):

        totalAmount = 0
        frequentRenterPoints = 0
        result = f"Rental Record for {self.__name}\n"
        for rental in self.__rentals:

            if rental.get_days_rented() > 0:

                thisAmount = rental.get_charge()

                # add frequent renter points
                frequentRenterPoints += 1

                # add bonus for a two day new release rental
                if rental.get_movie().price_code == Movie.NEW_RELEASE and rental.get_days_rented() > 1:
                    frequentRenterPoints += 1

                # show figures for this rental
                result += f" {rental.get_movie().get_title()}: {str(thisAmount)}\n"
                totalAmount += thisAmount

        # add footer lines
        result += f" Amount owed is {str(totalAmount)} \n"
        result += f" You earned {str(frequentRenterPoints)} frequent renter points \n"

        return result, totalAmount, frequentRenterPoints
