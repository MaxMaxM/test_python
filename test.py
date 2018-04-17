from person import Person
from manager import Manager

bob = Person(name='Bob Smith', age=42, pay=10000)
sue = Person(name='Sue Jones', age=45, pay=20000)
tom = Manager(name='Tom Due', age=55, pay=30000)
db = [bob, sue, tom]

for obj in db:
    obj.give_raise(.10) # the default or special method

for obj in db:
    print(obj.last_name(), '=>', round(obj.pay, 2))

