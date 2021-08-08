"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon ORders inherit from."""
    order_type = None
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        # self.order_type = None
        self.tax = None
    
    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if "christmas" in self.species or "Christmas" in self.species:
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        
        # flat_fee = (InternationalMelonOrder, self).get_total()
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon  order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """US Government order to pass security inspection"""
    
    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True


