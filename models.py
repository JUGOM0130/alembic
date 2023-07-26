from datetime import datetime
from sqlalchemy import Column, Integer, String,DateTime

# 自作モジュールの読み込み
from settings import BaseModel

class m_code(BaseModel):
    __tablename__ = 'm_code'
    
    cid = Column(Integer, primary_key=True,autoincrement=True)
    ckind = Column(Integer,nullable=False)
    chead = Column(String(10),nullable=False)
    cenumber = Column(String(5),nullable=False)
    cnumber = Column(Integer,nullable=False)
    cfoot = Column(String(10),nullable=False)
    
    def __repr__(self):
        return "<m_code('cid={}', ckind={}, chead={}, cenumber={}, cnumber={}, cfoot={})>".format(
            self.cid,
            self.ckind,
            self.chead,
            self.cenumber,
            self.cnumber,
            self.cfoot
        )
