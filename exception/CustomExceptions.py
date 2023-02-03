class NotFoundException(Exception):
    def __init__(self, value):            
        # Call the base class constructor with the parameters it needs
        super().__init__(value + " not found")

class AlreadyExistsException(Exception):
    def __init__(self, value):            
        # Call the base class constructor with the parameters it needs
        super().__init__(value + " already exists")

class InvalidStockException(Exception):
    def __init__(self, value):            
        # Call the base class constructor with the parameters it needs
        super().__init__(value + " is invalid")