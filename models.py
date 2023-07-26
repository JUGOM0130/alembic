from sqlalchemy import Column, Integer, String

# 自作モジュールの読み込み
from settings import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User('name={}', fullname={}, nickname={})>".format(
            self.name,
            self.fullname,
            self.nickname
        )
    
class Fruit(Base):
    __tablename__ = 'fruits'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return "<User('name={}', fullname={}, price={})>".format(
            self.name,
            self.fullname,
            self.price
        )
    

class Parts2(Base):
    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True)
    pname = Column(String)
    fullname = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return "<User('pname={}', fullname={}, price={})>".format(
            self.pname,
            self.fullname,
            self.price
        )
    