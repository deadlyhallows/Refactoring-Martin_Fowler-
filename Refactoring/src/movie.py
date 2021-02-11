class Movie:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title, priceCode):
        self.__title = title
        self.__price_code = priceCode

    def get_title(self):
        return self.__title

    @property
    def price_code(self):
        return self.__price_code

    @price_code.setter
    def price_code(self, value):
        self.__price_code = value
