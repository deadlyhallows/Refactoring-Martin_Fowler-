import pytest

from Refactoring.src.customer import Customer
from Refactoring.src.movie import Movie
from Refactoring.src.rental import Rental


class TestCustomer:

    """
    This class tests methods of Customer class
    """

    def test_statement_valid_args(self):
        """
        This tests if valid output is generated for valid output
        """

        movie_1 = Movie("abc", 0)
        movie_2 = Movie("def", 1)
        movie_3 = Movie("ghi", 2)

        rental_1 = Rental(movie_1, 1)
        rental_2 = Rental(movie_2, 2)
        rental_3 = Rental(movie_3, 3)

        customer = Customer("Awanti")

        for rental in [rental_1, rental_2, rental_3]:
            customer.add_rental(rental)

        statement, total_amount, pointers = customer.get_statement()

        assert (total_amount == 9.5)
        assert (pointers == 4)

    def test_statement_invalid_movie_price_code(self):

        """
        This tests statement method for invalid movie price code

        """

        with pytest.raises(ValueError) as exec_info:
            movie_1 = Movie("abc", 0)
            movie_2 = Movie("def", 1)
            movie_3 = Movie("ghi", 3)

            rental_1 = Rental(movie_1, 1)
            rental_2 = Rental(movie_2, 2)
            rental_3 = Rental(movie_3, 3)

            customer = Customer("Awanti")

            for rental in [rental_1, rental_2, rental_3]:
                customer.add_rental(rental)

            statement, total_amount, pointers = customer.get_statement()
            assert (total_amount == 8)
            assert (pointers == 4)

        exec_info.match("this type does not exists.")



    def test_statement_invalid_days_rented(self):
        """
        This tests statement method for invalid days rented for rentals

        """
        movie_1 = Movie("abc", 0)
        movie_2 = Movie("def", 1)
        movie_3 = Movie("ghi", 2)

        rental_1 = Rental(movie_1, -1)
        rental_2 = Rental(movie_2, 0)
        rental_3 = Rental(movie_3, 3)

        customer = Customer("Awanti")

        for rental in [rental_1, rental_2, rental_3]:
            customer.add_rental(rental)

        statement, total_amount, pointers = customer.get_statement()

        assert (total_amount == 1.5)
        assert (pointers == 1)
