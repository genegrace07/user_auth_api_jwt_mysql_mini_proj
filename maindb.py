import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('dbdatabase'),
    auth_plugin=os.getenv('dbauth_plugin')
)

class Users:
    def signup(self,username,password):
        db.ping(reconnect=True)
        dbcursor=db.cursor(dictionary=True,buffered=True)
        querry = 'insert into user_info(users,password) values(%s,%s)'
        dbcursor.execute(querry,(username,password))
        db.commit()
        dbcursor.close()
    def login(self,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select users,password from user_info where users=%s'
        dbcursor.execute(querry,(username,))
        result=dbcursor.fetchall()
        dbcursor.close()
        return result
    def update_password(self,password,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='update user_info set password=%s where users=%s'
        dbcursor.execute(querry,(password,username))
        db.commit()
        db.close()
        dbcursor.close()
    def delete_user(self,user_id):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='delete from user_info where id=%s'
        dbcursor.execute(querry,(user_id,))
        db.commit()
        db.close()
        dbcursor.close()
class Verify(Users):
    def check_username(self,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select users from user_info where users=%s'
        dbcursor.execute(querry,(username,))
        result=dbcursor.fetchone()
        dbcursor.close()
        return result
    def select_all(self,username):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select * from user_info where users=%s'
        dbcursor.execute(querry,(username,))
        result=dbcursor.fetchall()
        dbcursor.close()
        return result
    def select_users(self):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select users from user_info'
        dbcursor.execute(querry)
        result=dbcursor.fetchall()
        dbcursor.close()
        return result
    def all_users(self):
        db.ping(reconnect=True)
        dbcursor=db.cursor(buffered=True)
        querry='select id,users,created_at from user_info'
        dbcursor.execute(querry)
        result=dbcursor.fetchall()
        dbcursor.close()
        return result