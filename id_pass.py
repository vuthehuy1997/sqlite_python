import sqlite3

Admin_user_Table = 'Admin_user'
Room_Table = 'Room'
Room_activate_Table = 'Room_activate'

from sqlite3 import Error
class Sql_id_pass:
    def __init__(self, dataBase):
        self.con = self.sql_connection(dataBase)
    def sql_connection(self, dataBase):
        try:
            con = sqlite3.connect(dataBase)
            return con
        except Error:
            print(Error)
    def sql_table(self, tableName, content):
        cursorObj = con.cursor()
        # cursorObj.execute('drop table if exists ' + tableName)
        self.cursorObj.execute('create table if not exists '+tableName+content)
        self.con.commit()
    def sql_insert(self, tableName, entities):
        cursorObj = self.con.cursor()
        # cursorObj.execute('INSERT INTO '+tableName+ ' ' +columns+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
        self.cursorObj.execute('INSERT INTO '+tableName+' VALUES(?' + ', ?'*(len(entities)-1) +')', entities)
        self.con.commit()
    def sql_update(self, query):
        cursorObj = self.con.cursor()
        cursorObj.execute(query)
        self.con.commit()
    def sql_fetch(self, query):
        cursorObj = self.con.cursor()
        cursorObj.execute(query)
        rows = cursorObj.fetchall()
        return rows
    def sql_list_table(self):
        cursorObj = self.con.cursor()
        cursorObj.execute('SELECT name from sqlite_master where type= "table"')
        return (cursorObj.fetchall())

    def update_id_pass(self, email, room, meeting_id, password):
        rows = self.sql_fetch('SELECT * FROM "'+Room_Table + '" WHERE room = "' + room + '" AND admin = "' + email + '"')
        if len(rows) == 0:
            return False
        rows = self.sql_fetch('SELECT * FROM "'+Room_activate_Table + '" WHERE room = "' + room + '"')
        if len(rows) == 0:
            print('insert\n')
            self.sql_insert(Room_activate_Table, (room, meeting_id, password))
            return True
        else:
            print('update\n')
            self.sql_update('UPDATE "'+Room_activate_Table + '" SET meeting_id = "' + meeting_id + '", pass = "' + password + '" WHERE room = "' + room + '"')
            return True
    def get_id_pass(self, room):
        rows = self.sql_fetch('SELECT * FROM "'+Room_Table + '" WHERE room = "' + room + '" AND admin = "' + email + '"')
        if len(rows) == 0:
            return None, None
        rows = self.sql_fetch('SELECT * FROM "'+Room_activate_Table + '" WHERE room = "' + room + '"')
        if len(rows) == 1:
            return rows[0][1], rows[0][2]
        else :
            return None, None

ob = Sql_id_pass('ziim.db')

email, room, meeting_id, password = 'test@gmail.com', 'Math', 'meeting_id', 'new_pass2'
print(ob.update_id_pass(email, room, meeting_id, password))


print(ob.sql_fetch('SELECT * FROM Room_activate WHERE room = \'Math\''))

print(ob.get_id_pass(room))