import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('dbdatabase')
)

class Users:
    def signup(self,username,password):
        db.ping(reconnect=True)
        dbcursor=db.cursor(dictionary=True,buffered=True)
        querry = 'insert into user_info(users,password) values(%s,%s)'
        dbcursor.execute(querry,(username,password))
        db.commit()
        dbcursor.close()
        db.close()

class Verify(Users):
    def check_username(self,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select users from user_info where users=%s'
        dbcursor.execute(querry,(username,))
        result=dbcursor.fetchone()
        dbcursor.close()
        return result
