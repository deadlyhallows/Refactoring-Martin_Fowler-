from Refactoring.src.price import RegularPrice, NewReleasePrice, ChildrenPrice


class Movie:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title, priceCode):
        self.__title = title
        self.__price = None
        self.set_price_code(priceCode)

    def get_title(self):
        return self.__title

    def get_price_code(self):
        return self.__price.get_price_code()

    def set_price_code(self, value):
        if value == 0:
            self.__price = RegularPrice()
        elif value == 1:
            self.__price = NewReleasePrice()
        elif value == 2:
            self.__price = ChildrenPrice()
        else:
            raise ValueError("this type does not exists.")

    def get_charge(self, days_rented):
        return self.__price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented):
        return self.__price.get_frequent_renter_points(days_rented)
