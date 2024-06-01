import mysql.connector
def open():
    global conn
    global cursor
    conn=mysql.connector.connect(host='localhost',database='myshop_database',user='root',password='W7301@shiv#')
    cursor=conn.cursor()
def close():
    conn.commit()
    cursor.close();
    conn.close();

def fb.Login(username,code):
    open()
    query=f"select*from account where username='{username}' and code='{password}' "
    cursor.execute(query)
    rec=cursor.fetchall()
    if len(rec)>0:
        return True
    else:
        return False
    close()
