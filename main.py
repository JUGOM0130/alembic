from models import Fruit
from sesison import session



print(type(Fruit))
print(type(Fruit()))

print(Fruit)
print(Fruit())

a = session.query(Fruit).all()
print(a)