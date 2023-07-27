import sqlite3 
from sqlite3 import Error 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn 
def CreateTables (con) : 
    try : 
        cur=con.cursor () 
    except Error as e :
        print (e)
    cur.execute ("CREATE TABLE IF NOT EXISTS players (playe_rname CHAR , username CHAR , player_lastname CHAR, player_passwrd CHAR , rating INT )")
    con.commit ()
def ChangePlyaerAttributes (con , Field , Username , NewField) : 
    try : 
        cur=con.cursor () 
    except Error as e :
        print (e)
    cur.execute("UPDATE players SET '{}' = '{}' WHERE username = '{}'" .format(Field , NewField , Username))
def main () : 
    conn = create_connection ("ping_pong.db")
    CreateTables (conn)
if __name__=='__main__' : 
    main()