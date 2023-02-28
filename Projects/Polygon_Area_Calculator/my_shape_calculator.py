class Rectangle:
    '''
    This is a Python class definition for a Rectangle class that has a constructor method (__init__) 
    which takes two arguments width and height, and initializes two instance variables self.width and self.height 
    with the values of the corresponding arguments.
    '''
    def __init__(self, width, height):
        '''
        The __init__ method is a special method in Python classes that is called when an instance of the class is created. 
        It is used to set up the initial state of the object by setting its instance variables or performing other 
        initialization tasks.
        '''
        self.width = width
        self.height = height

    def set_width(self, width):
        '''
        This method updates the width attribute of a Rectangle object to a specified integer value. 
        It takes one parameter, width, which represents the new width value to be set. 
        This parameter should be an integer.
        '''
        self.width = width

    def set_height(self, height):
        '''
        This method updates the height attribute of a Rectangle object to a specified integer value. 
        It takes one parameter, height, which represents the new height value to be set. 
        This parameter should be an integer.
        '''
        self.height = height


    def get_width(self):
        '''
        This method returns the current width of a Rectangle object. It takes no parameters. 
        The return value of this method is an integer representing the current width of the Rectangle object.
        '''
        return self.width




# Testing Area
rect = Rectangle(5, 10)
print("rect width:", rect.width)
print("rect height:", rect.height)
rect.set_width(11)
print("Set width:", rect.width)
print("Get width:",rect.get_width())
