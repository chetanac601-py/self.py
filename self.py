class human :
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def constructor(self):
        print(f"my name is {self.name}. and my age is {self.age}")

human1 = human("chetan",18)
human1.constructor()
    

class laptop :
    def __init__(self,brand,price):
        self.brand= brand
        self.price = price

    def introduce(self):
        print(f"laptop brand:{self.brand},{self.price}")

laptop1=laptop("dell",4500)
laptop2=laptop("mac book",220000)

laptop1.introduce()
laptop2.introduce()
        

class movie:
    def __init__ (self,title,rating):
        self.title=title
        self.rating=rating

    def show_movie(self) :
        print(f"movie title:{self.title},movie rating:{self.rating}")

movie1=movie("kgf 1",5.0)
movie2=movie("salaar",4.5)

movie1.show_movie()
movie2.show_movie()
