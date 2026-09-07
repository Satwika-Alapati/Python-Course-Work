'''
class Flipkart:
    products={'shirts':1000,'handbag':2000,'pants':3000}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)
    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name},Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going-on,grab the products...")
david=Flipkart()
david.userinfo('david',9978456102,'Hyd')
david.displaydiscount()
david.display()
print(david.products)
print(david.name)

Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)

#using object->ins,cls,sta,clsatt,insatt
#using class->cls,sta,clsatt


jack=Flipkart()
jack.userinfo('jack',8899774411,'chennai')
jack.displaydiscount()
jack.display()
alex=Flipkart()
alex.userinfo('alex',8877552101,'guntur')
alex.displaydiscount()
alex.display()
'''
'''
class Flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f"Hello {self.name}, Welcome to the flipkart")

david=Flipkart('david',9978456102)
jack=Flipkart('jack',8899774411)
alex=Flipkart('alex',8877552101)
'''

class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self.__posts=[]

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password=newpassword
    
    @property
    def accesspost(self):
        return self.__posts

    @accesspost.setter
    def accesspost(self,newpost):
        self.__posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self.__posts)

david=Instagram('david','david@123')
david.display()
print(david.username)
print(david.getpassword())
print(david.accesspost)

david.username='jack'
david.setpassword("jack@123")
david.accesspost="sunrise.png"
david.accesspost="beach.png"
david.accesspost="forest.png"

print(david.username)
print(david.getpassword())
print(david.accesspost)
