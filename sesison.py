from sqlalchemy.orm import sessionmaker

import settings

SessionClass = sessionmaker(bind=settings.Engine)  # セッションを作るクラスを作成
session = SessionClass()
