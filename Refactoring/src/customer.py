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
        result = f"Rental Record for { self.__name }\n"
        for each in self.__rentals:
            price_code = each.get_movie().price_code
            days_rented = each.get_days_rented()
            thisAmount = 0
            if days_rented > 0:
                if price_code == Movie.REGULAR:
                    thisAmount += 2
                    if days_rented > 2:
                        thisAmount += (days_rented - 2) * 1.5
                if price_code == Movie.NEW_RELEASE:
                    thisAmount += days_rented * 3
                if price_code == Movie.CHILDRENS:
                    thisAmount += 1.5
                    if days_rented > 3:
                        thisAmount += (days_rented - 3) * 1.5

                # add frequent renter points
                frequentRenterPoints += 1

                # add bonus for a two day new release rental
                if price_code == Movie.NEW_RELEASE and days_rented > 1:
                    frequentRenterPoints += 1

                # show figures for this rental
                result += f" {each.get_movie().get_title()}: {str(thisAmount)}\n"
                totalAmount += thisAmount

        # add footer lines
        result += f" Amount owed is {str(totalAmount)} \n"
        result += f" You earned {str(frequentRenterPoints)} frequent renter points \n"

        return result, totalAmount, frequentRenterPoints
