class Bread:
    def __init__(self, flour_type: str, is_moldy: bool):
        self.flour_type= flour_type
        self.is_moldy = is_moldy

    def __str__(self):
        result = f"Flour: {self.flour_type};\n"
        result += f"Moldy: {self.is_moldy}"
        return result
    

class SaleItem:
        
        def __init__(self, price: float) -> None:
             self.price = price
        
        def __str__(self) -> str:
             return str(self.price)
        

class HamburgerBun(Bread, SaleItem):
     def __init__(self):
          Bread.__init__(self, 'Wheat', False)
          SaleItem.__init__(self, 3.50)



          