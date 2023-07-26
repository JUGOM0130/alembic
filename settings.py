'''
settings.py
DBの設定を行うファイル
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# path = 'sqlite:///db.sqlite3'
path = 'mysql+pymysql://root:root@127.0.0.1:33067/b_system'
 
# Engine の作成
Engine = create_engine(
  path,
  #encoding="utf-8",
  echo=False
)
Base = declarative_base()