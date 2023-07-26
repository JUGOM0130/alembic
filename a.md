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

## カラムの型など
* [Link](https://zenn.dev/shimakaze_soft/articles/6e5e47851459f5)
* [Alembic で create table する migration ファイルを auto gen する際にカラムの順番を調整する](https://qiita.com/nassy20/items/39b07e66b014fa5d9bb3)
* [BaseClass](https://blog.kumano-te.com/activities/sqlalchemy-tips)
* [これだBaseClass](https://qiita.com/penpenta/items/bd2940946324dedbd543)
* [型](https://zenn.dev/re24_1986/articles/8520ac3f9a0187)
* [currentTimestamp](https://qiita.com/arkuchy/items/8ae90e4a73ef30dc4749)