import mysql.connector
Info=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="social_media_analytics"
)
cursor=Info.cursor(buffered=True)
def sign_in(data):
    try:
        cursor.execute("SELECT * FROM `sign_in` WHERE`email_id`=%s AND `password`= %s",data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False
    
# table for forget password
def forget_password(data):
    try:
        cursor.execute("UPDATE `sign_in` SET `email_id`=%s,`password`=%s WHERE `email_id`=%s",data)
        Info.commit()
    except Exception as e:
        print (e)
        return False
    