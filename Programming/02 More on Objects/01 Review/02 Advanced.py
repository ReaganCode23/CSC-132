class House:

    MIN_PRICE = 0

    def __init__(self, price, sqft):
        self.price = price
        self.sqft = sqft
        self.roof_color = "black"
        self.num_floors: int  #type hints are useful, not necessary

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

    class QuadraticFunction:
    def __init__(self, a, b, c):
        self.a = coef_a
        self.b = b
        self.c = c

    @staticmethod
    def calc_property_tax(cls):
        return self.sqft * 20
    
    def __str__(self, other):
        return f"House - Price: {self.price}"
    def __add__(self, other: 'House') -> 'House':  #Tye hints are the house thing after semi coloumn.
       """What it means to add two houses together"""
       return self.price + other
    
    
h = House(10, 256)
h.price = 55

        
