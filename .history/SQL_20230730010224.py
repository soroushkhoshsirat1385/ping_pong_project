import ping_pong as pg
import sqlite3 
from sqlite3 import Error
 

conn = None
try:
    conn = sqlite3.connect("ping_pong.db")
    print(sqlite3.version)
except Error as e:
    print(e) 
def CreateTables () : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute ("CREATE TABLE IF NOT EXISTS players (playe_rname TEXT , username TEXT , player_lastname TEXT, player_passwrd TEXT , rating INT )")
    conn.commit ()
def AddPlayer (player : pg.player) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute("""INSERT INTO players VALUES ('{}' , '{}' , '{}' , '{}' , {})""".format(player.Name , player.UserName , player.LastName , player.Password , player.Rating))
    conn.commit ()
def ChangePlyaerAttributes ( Field , Username , NewField) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute("UPDATE players SET '{}' = '{}' WHERE username = '{}'" .format(Field , NewField , Username))
    conn.
def main () : 
    CreateTables ()
if __name__=='__main__' : 
    main()