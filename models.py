from sqlalchemy import Column, Integer, String, VARCHAR

# 自作モジュールの読み込み
from settings import BaseModel

class MCode(BaseModel):
    __tablename__ = 'm_code'
    
    cid = Column(Integer, primary_key=True,autoincrement=True,comment="コードID")
    ckind = Column(Integer,nullable=False,comment="種別")
    chead = Column(String(10),nullable=False,comment="ヘッダ")
    cenumber = Column(String(5),nullable=False,comment="英番号")
    cnumber = Column(Integer,nullable=False,comment="通番号")
    cfoot = Column(String(10),nullable=False,comment="フッダー")
    
    def __repr__(self):
        return "<m_code('cid={}', ckind={}, chead={}, cenumber={}, cnumber={}, cfoot={})>".format(
            self.cid,
            self.ckind,
            self.chead,
            self.cenumber,
            self.cnumber,
            self.cfoot
        )
class MCodeTemplate(BaseModel):
    __tablename__ = 'm_code_template'
    ctid=Column(Integer,primary_key=True,autoincrement=True,comment="テンプレートID")
    ctkind=Column(Integer,nullable=False,comment="種別")
    cthead=Column(VARCHAR(10),nullable=False,comment="ヘッダ")
    ctenumber=Column(VARCHAR(5),nullable=False,comment="英番号")

    def __repr__(self):
        return "<m_code_template('ctid={}','ctkind={}','cthead={}','ctenumber={}')>".format(
            self.ctid,
            self.ctkind,
            self.cthead,
            self.ctenumber
        )
class MPart(BaseModel):
    __tablename__ = 'm_parts'
    pid=Column(Integer,primary_key=True,autoincrement=True,comment="パーツID")
    pcid=Column(Integer,nullable=False,comment="")
    pcd=Column(VARCHAR(45),nullable=False,comment="")
    pname=Column(VARCHAR(45),nullable=False,comment="")
    ppname=Column(VARCHAR(45),nullable=False,comment="")
    prevision= Column(VARCHAR(45),nullable=False,comment="")
    pvendor= Column(VARCHAR(45),nullable=False,comment="")
    ptype= Column(VARCHAR(45),nullable=False,comment="")
    pmaterial= Column(VARCHAR(45),nullable=False,comment="")
    pio= Column(VARCHAR(45),nullable=False,comment="")
    pmtlmain_cost= Column(VARCHAR(45),nullable=False,comment="")
    pmtlsub_cost= Column(VARCHAR(45),nullable=False,comment="")
    pprocdict_cost= Column(VARCHAR(45),nullable=False,comment="")
    pprocsub_cost= Column(VARCHAR(45),nullable=False,comment="")


    def __repr__(self):
        return "<m_code_template('ctid={}','ctkind={}','cthead={}','ctenumber={}')>".format(
            self.ctid,
            self.ctkind,
            self.cthead,
            self.ctenumber