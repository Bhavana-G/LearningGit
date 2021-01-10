class Book():
    favs = [] #class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return True

    #What happens when you pass object to print?
    def __str__(self):
        return f'{self.title}, {self.pages} pages long'

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True
    #It's appropriate to give something for __hash__ when you override __eq__
    #This is the recommended way if mutable(like it is here):
    __hash__ = None

    #added to make list of items invoke str
    def __repr__(self): #used to display objects
        return self.__str__() #used to display object contents in user friendly manner