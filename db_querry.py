import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('dbhost'),
    user=os.getenv('dbuser'),
    password=os.getenv('dbpassword'),
    database=os.getenv('dbdatabase'),
    auth_plugin=os.getenv('dbauth_plugin')
)


dbcursor = db.cursor(dictionary=True)
dbcursor.execute('select * from user_details')
result = dbcursor.fetchall()
print(result)