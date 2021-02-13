class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = list()

    def add_rental(self, rental):
        self.__rentals.append(rental)

    def get_total_frequent_renter_points(self):
        total_renter_points = 0
        for rental in self.__rentals:
            if rental.get_days_rented() > 0:
                total_renter_points += rental.get_frequent_renter_points()

        return total_renter_points

    def get_total_amount(self):
        total_amount = 0
        for rental in self.__rentals:
            if rental.get_days_rented() > 0:
                total_amount += rental.get_charge()

        return total_amount

    def get_statement(self):

        result = f"Rental Record for {self.__name}\n"
        for rental in self.__rentals:

            if rental.get_days_rented() > 0:

                # show figures for this rental
                result += f" {rental.get_movie().get_title()}: {str(rental.get_charge())}\n"

        # add footer lines
        result += f" Amount owed is {str(self.get_total_amount())} \n"
        result += f" You earned {str(self.get_total_frequent_renter_points())} frequent renter points \n"

        return result, self.get_total_amount(), self.get_total_frequent_renter_points()

    def get_html_statement(self):

        result = f"<H1>Rentals for <EM> {self.__name} </EM></H1><P>\n"
        for rental in self.__rentals:

            if rental.get_days_rented() > 0:

                # show figures for this rental
                result += f" {rental.get_movie().get_title()}: {str(rental.get_charge())} <BR>\n"

        # add footer lines
        result += f" <P>Amount owed<EM> is {str(self.get_total_amount())} </EM></P>\n"
        result += f" <P><EM>You earned {str(self.get_total_frequent_renter_points())} " \
                  f"frequent renter points </EM></P>\n"

        return result, self.get_total_amount(), self.get_total_frequent_renter_points()
