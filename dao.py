
import pymysql.cursors


#データベースへの接続に必要な情報を指定して、接続するためのメソッド
#connectionに接続したデータベース情報が代入される

def connect():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="pybase",
        cursorclass=pymysql.cursors.DictCursor
        #ディクショナリ型でデータを受け取る
    )
    return connection


#with文のブロック内にデータベース操作のための処理を記述
# SQL文を用意(文字列で用意する)
# 用意したSQL文を接続中のデータベースに対して実行(execute)
#SELECT文でレコード全件取得
def find_all():
    result = None
    with connect() as con:
        with con.cursor() as cursor:
            sql="SELECT * FROM ranking ORDER BY SCORE DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            #fetchall関数
            #SELECT文を実行したとき、データベースのテーブルからデータが返ってきている
            #かえってきたデータを受け取るために呼び出すメソッド
            #戻り値はタプル、中の要素はレコード１つにつきディクショナリ１つにまとまっている
            #カラム名がディクショナリのキーになっている
            return result

# テーブルにデータ１件追加
def insert_one(user):
    with connect() as con:
        with con.cursor() as cursor:
            sql ="INSERT ranking(name,score) VALUES(%s, %s)"
            cursor.execute(sql,(user["name"],user["score"]))
            #タプルの中に、user[name]
            con.commit()#変更をデータベースに伝える
        
            
"""
"""


