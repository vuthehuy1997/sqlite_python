import sqlite3

from sqlite3 import Error

def sql_connection(dataBase):
    try:
        con = sqlite3.connect(dataBase)
        return con
    except Error:
        print(Error)
def sql_table(con, tableName, content):
    cursorObj = con.cursor()
    cursorObj.execute('drop table if exists ' + tableName)
    cursorObj.execute('create table if not exists '+tableName+content)
    con.commit()
def sql_insert(con, tableName, entities):
    cursorObj = con.cursor()
    # cursorObj.execute('INSERT INTO '+tableName+ ' ' +columns+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
    cursorObj.execute('INSERT INTO '+tableName+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
    con.commit()

def sql_fetch(con, tableName):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM '+tableName+'')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

dataBase = 'ziim.db'
Admin_user_Table = 'Admin_user'
Room_Table = 'Room'
Room_activate_Table = 'Room_activate'

con = sql_connection(dataBase)
Admin_user_Columns = ['email','name','payment']
Room_Columns = ['room', 'admin']
Room_activate_Columns = ['room', 'meeting_id', 'pass']
User_Columns  = ['email', 'room']

sql_table(con, Admin_user_Table,'(email text PRIMARY KEY, name text, payment text)')
sql_table(con, Room_Table,'(room text PRIMARY KEY, admin text)')
sql_table(con, Room_activate_Table,'(room text PRIMARY KEY, meeting_id text, pass text)')

entities = ('test@gmail.com', 'God', '113')
sql_insert(con,Admin_user_Table, entities)

entities = ('Math', 'test@gmail.com')
sql_insert(con,Room_Table, entities)
entities = ('Math 2', 'test@gmail.com')
sql_insert(con,Room_Table, entities)

con.close()
