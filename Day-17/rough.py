class User:
    def __init__(self,userid,username,h):
        self.id=userid
        self.username=username
        self.height=h

user_1=User(1,"a","j")
print(user_1.height)

class Car:
    pass
car=Car()
car.name="bugati"
car.id=1

car2=Car()
car2.name="chiron"
car2.userid=2
print(car2.userid)
print(car.id)