from abc import ABC, abstractmethod


class Price(ABC):

    @abstractmethod
    def get_price_code(self):
        pass

    @abstractmethod
    def get_charge(self, days_rented):
        pass

    @abstractmethod
    def get_frequent_renter_points(self, days_rented):
        pass


class RegularPrice(Price):

    def get_price_code(self):
        return 0

    def get_charge(self, days_rented):
        thisAmount = 2
        if days_rented > 2:
            thisAmount += (days_rented - 2) * 1.5
        return thisAmount

    def get_frequent_renter_points(self, days_rented): return 1


class NewReleasePrice(Price):
    def get_price_code(self):
        return 1

    def get_charge(self, days_rented):
        return days_rented * 3

    def get_frequent_renter_points(self, days_rented):
        return 2 if days_rented > 1 else 1


class ChildrenPrice(Price):

    def get_price_code(self):
        return 2

    def get_charge(self, days_rented):
        thisAmount = 1.5
        if days_rented > 3:
            thisAmount += (days_rented - 3) * 1.5
        return thisAmount

    def get_frequent_renter_points(self, days_rented): return 1
