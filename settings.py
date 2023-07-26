'''
settings.py
DBの設定を行うファイル
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base,declared_attr


from sqlalchemy import Column,DateTime
from datetime import datetime

# path = 'sqlite:///db.sqlite3'
path = 'mysql+pymysql://root:root@127.0.0.1:33067/b_system'
 
# Engine の作成
Engine = create_engine(
  path,
  echo=True#SQLをログに出力するらしい
)

# すべてのDBに共通で作成するカラムをここで定義
class Base(object):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, default=datetime.now(), nullable=False, onupdate=datetime.now())

BaseModel = declarative_base(cls=Base)
