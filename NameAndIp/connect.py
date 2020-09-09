import os
import sqlite3
db_path = os.path.join(os.path.dirname(__file__), 'any.db')

class Table:

    conn = sqlite3.connect(db_path)
    def create_table(self):
        Table.conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS NAMES (
                NAME CHAR(50) PRIMARY KEY NOT NULL,
                IP CHAR(30) NOT NULL UNIQUE
            );
            '''
        )
        Table.conn.close()

    def insert_in_table(self, name, ip):

        Table.conn.execute(
            '''INSERT INTO NAMES (NAME, IP) VALUES(
                ?, ?
            )''', (name, ip));
        Table.conn.commit()
        Table.conn.close()

    def show_all_records(self):
        cursor = Table.conn.execute(
            'SELECT * FROM NAMES'
        )
        for row in cursor.fetchall():
            yield row
        Table.conn.close()

    def get_user_choice(self, user_choice):
        cursor = Table.conn.execute(
            'SELECT * FROM NAMES WHERE NAME LIKE ?'
        , ('%' + user_choice + '%', ))
        for row in cursor.fetchall():
            yield row
        Table.conn.close()

    def change_target(self, old_name, new_ip):
        cursor = Table.conn.execute(
            'UPDATE NAMES SET ip = ? WHERE NAME = ?'
        , (new_ip, old_name))
        Table.conn.commit()
        Table.conn.close()

    def delete_target(self, name):
        cursor = Table.conn.execute(
            'DELETE FROM NAMES WHERE NAME = ?'
        , (name, ))
        Table.conn.commit()
        Table.conn.close()



if __name__ == '__main__':
    t = Table()
    t.insert_in_table('test 2', '132')
    #t.create_table()