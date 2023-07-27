from sesison import session
import models



"""
テストデータのインサート
"""
def insert():
    m_code = models.MCode()
    m_code.cid = None
    m_code.ckind = 1
    m_code.chead = "ALD"
    m_code.cenumber = "A"
    m_code.cnumber = 1
    m_code.cfoot = "Z000"

    session.add(m_code)
    session.commit()
    session.close()

"""
全データ削除
"""
def alldelete():
    session.query(models.MCode).delete() # 全件
    # session.query(models.MCode).filter(models.MCode.cid==1).delete() # 条件付き
    session.commit()
    session.close()

"""
特定データ
"""
def update():
    rec = session.query(models.MCode).filter(models.MCode.cid==2).first()
    if(rec != None):
        rec.cfoot = "Z001"
        session.commit()
        session.close()
        print("更新完了")
    else:
        print("更新データ無し")