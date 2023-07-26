from sqlalchemy import Column, Integer, String, VARCHAR

# 自作モジュールの読み込み
from settings import BaseModel


class MCode(BaseModel):
    __tablename__ = 'm_code'

    cid = Column(Integer, primary_key=True,
                 autoincrement=True, comment="コードID")
    ckind = Column(Integer, nullable=False, comment="種別")
    chead = Column(String(10), nullable=False, comment="ヘッダ")
    cenumber = Column(String(5), nullable=False, comment="英番号")
    cnumber = Column(Integer, nullable=False, comment="通番号")
    cfoot = Column(String(10), nullable=False, comment="フッダー")

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
    ctid = Column(Integer, primary_key=True,
                  autoincrement=True, comment="テンプレートID")
    ctkind = Column(Integer, nullable=False, comment="種別")
    cthead = Column(VARCHAR(10), nullable=False, comment="ヘッダ")
    ctenumber = Column(VARCHAR(5), nullable=False, comment="英番号")

    def __repr__(self):
        return "<m_code_template('ctid={}','ctkind={}','cthead={}','ctenumber={}')>".format(
            self.ctid,
            self.ctkind,
            self.cthead,
            self.ctenumber
        )


class MPart(BaseModel):
    __tablename__ = 'm_parts'
    pid = Column(Integer, primary_key=True,
                 autoincrement=True, comment="パーツID")
    pcid = Column(Integer, nullable=False, comment="cidの外部キー")  # FK
    pcd = Column(VARCHAR(45), nullable=False, comment="パーツコード")
    pname = Column(VARCHAR(45), nullable=False, comment="パーツ名")
    ppname = Column(VARCHAR(45), nullable=False, comment="パーツ一般名")
    prevision = Column(VARCHAR(45), nullable=False, comment="リビジョン")
    pvendor = Column(VARCHAR(45), nullable=False, comment="取引先コード")  # FK
    ptype = Column(VARCHAR(45), nullable=False, comment="型式")
    pmaterial = Column(VARCHAR(45), nullable=False, comment="材料名")
    pio = Column(VARCHAR(45), nullable=False, comment="内外策")
    pstatus = Column(Integer, nullable=False, comment="ステータス")
    pmtlmain_cost = Column(Integer, nullable=False, comment="主要材料コスト")
    pmtlsub_cost = Column(Integer, nullable=False, comment="補助材料コスト")
    pprocdict_cost = Column(Integer, nullable=False, comment="外注加工費")
    pprocsub_cost = Column(Integer, nullable=False, comment="直接労務費")

    def __repr__(self):
        return "<m_parts('pid={}','pcid={}','pcd={}','pname={}','ppname={}','prevision={}','pvendor={}','ptype={}','pmaterial={}','pio={}','pmtlmain_cost={}','pmtlsub_cost={}','pprocdict_cost={}','pprocsub_cost={}')>".format(
            self.pid,
            self.pcid,
            self.pcd,
            self.pname,
            self.ppname,
            self.prevision,
            self.pvendor,
            self.ptype,
            self.pmaterial,
            self.pio,
            self.pmtlmain_cost,
            self.pmtlsub_cost,
            self.pprocdict_cost,
            self.pprocsub_cost
        )


class MStaff(BaseModel):
    __tablename__ = 'm_staff'
    scode = Column(Integer, primary_key=True,
                   autoincrement=True, comment="社員番号")
    sname1 = Column(VARCHAR(100), nullable=False, comment="氏")
    sname2 = Column(VARCHAR(100), nullable=False, comment="字")
    sname3 = Column(VARCHAR(100), nullable=False, comment="氏（カナ）")
    sname4 = Column(VARCHAR(100), nullable=False, comment="字（カナ）")

    def __repr__(self):
        return "<m_staff('scode={}','sname1={}','sname2={}','sname3={}','sname4={}')>".format(
            self.scode,
            self.sname1,
            self.sname2,
            self.sname3,
            self.sname4
        )


class MTori(BaseModel):
    __tablename__ = 'm_tori'
    tid = Column(Integer, primary_key=True,
                 autoincrement=True, comment="取引先ID")
    tname1 = Column(VARCHAR(100), nullable=False, comment="取引先名")
    tname2 = Column(VARCHAR(100), nullable=False, comment="取引先名（カナ）")
    zipcode = Column(VARCHAR(10), nullable=False, comment="住所")
    address1 = Column(VARCHAR(100), nullable=False, comment="県")
    address2 = Column(VARCHAR(100), nullable=False, comment="市区町村")
    address3 = Column(VARCHAR(100), nullable=False, comment="番地")
    address4 = Column(VARCHAR(100), nullable=False, comment="アパート・ビル名")
    tel1 = Column(VARCHAR(20), nullable=False, comment="電話番号")

    def __repr__(self):
        return "<m_tori('tid={}','tname1={}','tname2={}','zipcode={}','address1={}','address2={}','address3={}','address4={}','tel1={}')>".format(
            self.tid,
            self.tname1,
            self.tname2,
            self.zipcode,
            self.address1,
            self.address2,
            self.address3,
            self.address4,
            self.tel1
        )


class TTTable(BaseModel):
    __tablename__ = 't_tree_table'
    tree_id = Column(VARCHAR(100), primary_key=True,
                     nullable=False, comment="ツリーID")  # FK

    composition_id = Column(VARCHAR(100), nullable=False, comment="構成ID")
    parts_id = Column(VARCHAR(100), nullable=False, comment="字")
    lv = Column(VARCHAR(100), nullable=False, comment="氏（カナ）")
    parent_id = Column(VARCHAR(100), nullable=False, comment="字（カナ）")
    order = Column(Integer,nullable=False,comment="並び順")
    insu =Column(Integer,nullable=False,comment="員数")
    bosu =Column(Integer,nullable=False,comment="母数")

    def __repr__(self):
        return "<t_tree_table('tree_id={}','composition_id={}','parts_id={}','lv={}','parent_id={}','order={}','insu={}','bosu={}')>".format(
            self.tree_id,
            self.composition_id,
            self.parts_id,
            self.lv,
            self.parent_id,
            self.order,
            self.insu,
            self.bosu
        )
