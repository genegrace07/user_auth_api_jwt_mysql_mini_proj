import mysql.connector
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('auth_api')
)

dbcursor = db.cursor(dictionary=True)
dbcursor.execute('select * from auth_api')
result = dbcursor.fetchall()
print(result)