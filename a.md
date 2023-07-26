## requirements.txt
pip install slqalchemy alembic pymysql

## サイトを見て違ったところ
* engine変数生成時にencodingを指定するとエラーする


## マイグレーションファイル名を日付にする
* alembic.iniを編集
* file_templateの行をコメントアウトして好みに編集

## めちゃくちゃ詰まった場所
* env.pyにはモデルクラスをimportしておく必要がある
* ```session.query(Fruit).all()```
  * 上記コマンドの場合Fruitの型<class 'sqlalchemy.orm.decl_api.DeclarativeMeta'>
  * Fruitクラスのインスタンスを渡すのではないことに注意


## 基本的なコマンド
* マイグレーションファイルを作成
  * ```alembic revision --autogenerate -m "create table"```
* マイグレーションの実行
  * ```alembic upgrade head```
* ロールバック
  * ```alembic downgrade ID``` 指定のIDまで戻す
  * ```alembic downgrade base``` 最初に戻す