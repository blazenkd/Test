class Rectangle:
    '''
    Represents a rectangle.

    The Rectangle class initializes a rectangular shape with a given width and height. 
    It provides methods to compute the area, perimeter, diagonal, and picture of the rectangle.

    Attributes
    ----------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.
    '''
    def __init__(self, width, height):
        '''
        Initializes a new Rectangle object with the given width and height.

        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        '''
        self.width = width
        self.height = height

    def set_width(self, width):
        '''
        Sets the width of the Rectangle object.

        Parameters
        ----------
        width : int
            The desired width of the Rectangle object.
        '''
        self.width = width

    def set_height(self, height):
        '''
        Sets the height of the Rectangle object.

        Parameters
        ----------
        height : int
            The desired height of the Rectangle object.
        '''
        self.height = height

    def get_width(self):
        '''
        Returns the width of the Rectangle object.

        Returns
        -------
        int
            Width of the Rectangle object.
        '''
        return self.width

    def get_height(self):
        '''
        Returns the height of the Rectangle object.

        Returns
        -------
        int
            Height of the Rectangle object.
        '''
        return self.height

    def get_area(self):
        '''
        Calculates the area of the rectangle.

        Returns
        -------
        int
            The area of the rectangle, given by multiplying the width by the height.
        '''
        return (self.width * self.height)

    def get_perimeter(self):
        '''
        Returns the perimeter of the rectangle.

        Returns
        -------
        int
            The perimeter of the rectangle, which is calculated as 2 times the width plus 2 times the height.
        '''
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        '''
        Computes the diagonal of the Rectangle object using the Pythagorean theorem.

        Returns
        -------
        float
            The length of the diagonal of the rectangle.
        '''
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        '''Returns a string that represents the shape using lines of "*".

        The number of lines should be equal to the height and the number of "*" in each line should be equal to the width.
        There should be a new line (\n) at the end of each line.
        If the width or height is larger than 50, this should return the string: "Too big for picture.".

        Returns
        -------
        str
            A string that represents the shape using lines of "*".
        '''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.height):
                picture += "*" * self.width + "\n"
            return picture

    def get_amount_inside(self, other):
        '''
        Calculates the number of times a given shape (square or rectangle) can fit
        inside the current rectangle object without rotation.

        Parameters
        ----------
        other : object
            Another rectangle or square object to be placed inside the current rectangle.

        Returns
        -------
        int
            The number of times the given shape can fit inside the current rectangle.
        '''
        
        if self.width < other.width or self.height < other.height:
            return 0
        
        width_ratio = self.width // other.width
        height_ratio = self.height // other.height
        
        return width_ratio * height_ratio

    def __repr__(self):
        '''
        Returns a string representation of the Rectangle object that can be used
        to recreate the object.

        Returns
        -------
        str
            String representation of the Rectangle object.
        '''
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    '''
    A subclass of the Rectangle class representing a square shape. 

    The Square object is initialized with a single side length value. 
    It inherits the properties of the Rectangle class, including the 
    methods to calculate the area, perimeter, diagonal, and the picture
    of the shape.

    Attributes
    ----------
    side : int
        The length of a side of the square.

    Methods
    -------
    __init__(side)
        Initializes the Square object with a given side length.
    __repr__()
        Returns a string representation of the Square object.
    get_picture()
        Returns a string representation of the Square object as a picture made of '*'.
    '''
    def __init__(self, side):
        """Creates a Square object with a given side length.

        Parameters
        ----------
        side : int
            The length of the square's side.
        """
        self.width = side
        self.height = side    

    def set_side(self, side):
        """Set the side length of the Square object.

        Parameters
        ----------
        side : int
            An integer representing the length of the sides of the square.
        """
        self.width = side
        self.height = side

    def __repr__(self):
        '''
        Returns a string representation of the Square object that can be used
        to recreate the object.

        Returns
        -------
        str
            String representation of the Square object.
        '''
        return f"Square(side={self.width})"

# Testing Area
# rect = Rectangle(5, 10)
# print("rect width:", rect.width)
# print("rect height:", rect.height)
# rect.set_width(6)
# rect.set_height(11)
# print("Get width:",rect.get_width())
# print("Get Height:", rect.get_height())
# print("Get Area:", rect.get_area())
# print("Get Perimeter:", rect.get_perimeter())
# print("Get Picture:", rect.get_picture())
# print("Get Amount Inside:", rect.get_amount_inside(Rectangle(2,2)))
# print(rect)
# square = Square(4)
# print("Square width:", square.width)
# print("Square height:", square.height)
# square.set_side(5)
# print("Square width:", square.width)
# print("Square height:", square.height)
# print(square)