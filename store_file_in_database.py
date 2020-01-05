"""
When start script check password is corect if true,
may attach file to database or list attached files from database
"""

# Import Modules
from hashlib import sha256          # Generate secret password
import sys                          # Use for exit
import sqlite3                      # Database is sqlite

# sha256 password slice to 15 symbol
SECRET_PASSWORD = "10e357984b55966"


# Function's
def create_or_alter_table():
    """Create table if not exists"""

    try:
        con = sqlite3.connect('db_file.db')
    except sqlite3.Error as e:
        print(e)
    else:
        c = con.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS ideqs
        (id INTEGER PRYMARY KEY AUTOINCREMENT, name text NOT NULL,
        extension text NOT NULL)'''
        c.execute(sql)
        con.commit()
    finally:
        return con


def func_to_save_file_in_database():
    """Save path to database"""

    con = create_or_alter_table()
    c = con.cursor()
    files = input("Enter path to file :")
    path, extension = files.split(".")
    command = """INSERT INTO ideqs (name, extension) VALUES (?, ?)"""
    c.execute(command, (files, extension,))
    con.commit()


def func_to_load_file_from_database():
    """Return files from database"""

    con = create_or_alter_table()
    c = con.cursor()
    sql = """SELECT * FROM ideqs"""
    c.execute(sql)
    for line in c.fetchall():
        print(line[1], line[2])


def ask_what_you_need():
    print("-"*20)
    print("""
    S|s to store file in database
    L|l to load file from database
    Q|q to quit
    """)
    print("-"*20)
    user = input("Enter what you whant :")

    choices = {"s": func_to_save_file_in_database,
               "l": func_to_load_file_from_database}

    if user.lower() in choices.keys():
        choices[user.lower()]()
    else:
        sys.eixt()


if __name__ == '__main__':
    enter_password = sha256(sys.argv[1].encode("utf-8")).hexdigest()[:15]

    if (enter_password[:15] != SECRET_PASSWORD):
        sys.exit()

    ask_what_you_need()
