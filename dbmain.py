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
        dbcursor=db.cursor(buffered=True)
        querry='insert into user_details(username,password) values(%s,%s)'
        result=dbcursor.execute(querry(username,password))
        db.commit()
        dbcursor.close()

