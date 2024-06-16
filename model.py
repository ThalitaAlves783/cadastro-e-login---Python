from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  
import pymysql.cursors

con = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "32834164",
    port = 3306,
    db = "projetologin",
    charset="utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)

try:
    with con.cursor() as cursor:
        cursor.execute("create table teste (nome varchar(50))")
    print("deu bom")
except Exception as e:
    print(f'Deu ruim {e}')

con.close()