from decimal import Decimal, ROUND_UP

medicals = ['headache pills', ]
food = ['chocolates', 'chocolate bar', 'box of chocolates', ]


def round_off(value):
    value = Decimal(value)
    return float((value * 2).quantize(Decimal('.2'), rounding=ROUND_UP) / 2)


class Tax:
    def __init__(self, percent, exempt_items=None):
        self.percent = percent
        self.exempt_items = exempt_items

    def is_exempt(self, product_name):
        pass

    def calculate_tax(self, product):
        if not self.is_exempt(product.name):
            return round_off(str(product.price * self.percent))
        return 0.0


class BaseTax(Tax):
    def __init__(self, percent, exempt_items=None):
        super(BaseTax, self).__init__(percent, exempt_items)

    def is_exempt(self, product_name):
        if product_name in self.exempt_items:
            return True
        return False


class ImportTax(Tax):
    def __init__(self, percent, exempt_items=None):
        super(ImportTax, self).__init__(percent, exempt_items)

    def is_exempt(self, product_name):
        if 'imported' not in product_name:
            return True
        return False


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def calculate_taxed_price(self):
        tax = BaseTax(0.1, medicals + food + ['book']).calculate_tax(self) + ImportTax(0.05).calculate_tax(self)
        return float(round_off(str(self.price + tax))), tax


def generate_receipt(items):
    total_price = 0.0
    total_tax = 0.0
    for item in items:
        product = item.split(" ")
        product.remove("at")
        quantity = int(product[0])
        price = float(product[-1])
        name = " ".join(product[1:-1])
        product_obj = Product(name, quantity, price)
        product_taxed_price, tax = product_obj.calculate_taxed_price()
        total_price += product_taxed_price
        total_tax += tax
        print(f"{quantity} {name}: {product_taxed_price}")

    print(f"Sales Tax: {total_tax}")
    print(f"Total: {total_price}")


if __name__ == "__main__":
    input_items = [
        "1 book at 12.49",
        "1 music CD at 14.99",
        "1 chocolate bar at 0.85"
    ]

    generate_receipt(input_items)
