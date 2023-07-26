class Student:
    """
    A class that represent a student with private fields id, 
       firstname and lastname.
       Provide getter and setter methods.
    """
    def __init__(self, id, firstname, lastname):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname

    # Getters and setters
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def firstname(self):
        return self.__firstname
    
    @id.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @property
    def lastname(self):
        return self.__lastname
    
    @id.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    

