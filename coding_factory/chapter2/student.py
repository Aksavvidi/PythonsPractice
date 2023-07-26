# Δήλωση μεταβλητών
class Student:
    """
    A Clas that represents a person with firstname and lastname
    Attributes: 
     - Firstname(str) : the firstname of the person
     - Lastname (str) : the lastname of the person
    """
    def __init__(self, firstname, lastname):
        """
        Initialize a ne instance of the Person Class.
        Args:
        - Firstname(str) : the firstname of the person
        - Lastname (str) : the lastname of the person
        """
        self.firstname = firstname
        self.lastname = lastname
