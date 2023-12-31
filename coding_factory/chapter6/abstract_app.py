class AbstractStudentDAO:
    """
    Defines the student DAO API
    """

    def insert(self):
        raise NotImplementedError()
    
    def update(self):
        raise NotImplementedError()
    
    def delete(self):
        raise NotImplementedError()
    
    def getOne(self):
        raise NotImplementedError()
    
class StudentImpl(AbstractStudentDAO):
    def insert(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
    def getOne(self):
        pass

from abc import ABC, abstractmethod
from store import Item, OutOfStockError

# Public    API
class ABCInventory(ABC):

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        pass

class Inventory(ABCInventory):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name_to_remove):
        if Item(item_name_to_remove, None) not in self.items:
            raise ValueError(f"{item_name_to_remove} is not in the inventory.")
        
        for item in self.items:
            if item == Item(item_name_to_remove, None):
                if item.quantity >0:
                    item.quantity -= 1
                    return Item(item.name, item.quantity)
            else:
                raise OutOfStockError(item.name)

    def print_items(self):
        for item in self.items:
            print(item)
        
