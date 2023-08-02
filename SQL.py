import ping_pong as pg
import sqlite3 
from sqlite3 import Error
import uuid 
import datetime
import consts as consts
try:
    conn = sqlite3.connect("ping_pong.db")
    print(sqlite3.version)
except Error as e:
    print(e) 
def ReturnConfigByID (ID) : 
    pass
def CreateTables () : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute ("CREATE TABLE IF NOT EXISTS players (player_name TEXT , username TEXT , player_lastname TEXT, player_password TEXT , rating INT )")
    conn.commit ()
    cur.execute("CREATE TABLE IF NOT EXISTS games (player1_username TEXT , player2_username TEXT , game_start_time TEXT , score TEXT , game_ID  INT)")
    conn.commit ()
    cur.execute("CREATE TABLE IF NOT EXISTS configs (game_id TEXT ,rounds INT , PPR INT , TPG INT , TOD FLOAT)")
    conn.commit()
def AddPlayer (player : pg.player) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute("""INSERT INTO players VALUES ('{}' , '{}' , '{}' , '{}' , {})""".format(player.Name , player.UserName , player.LastName , player.Password , player.Rating))
    conn.commit ()
    print ("added a new player")
def RemovePlayer(player : pg.player ) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute("""DELETE FROM players WHERE username='{}'""".format(player.UserName))
    
    conn.commit()
def AddConfig (game:pg.game , ID : int) : 
    try : 
        cur = conn.cursor() 
    except Error as a : 
        print(a) 
    cur.execute("""INSERT INTO configs VALUES ('{}' , {} , {} , {} , {})""".format(ID , game.config.rounds , game.config.PPR , game.config.TPG , game.config.TOD))
    conn.commit()
def AddGame (game:pg.game) : 
    try : 
        cur = conn.cursor() 
    except Error as a : 
        print(a) 
    ID = uuid.uuid4() 
    e = datetime.datetime.now ()
    time = e.strftime("%Y-%m-%d %H:%M:%S") 
    cur.execute ("""INSERT INTO games VALUES ('{}' , '{}' , '{}' , '{}' , '{}')""".format(game.player1.UserName , game.player2.UserName , time , "0-0" , ID))
    conn.commit() 
    print ("added a new game")
    AddConfig (game , ID)
    return ID 
def ChangePlyaerAttributes ( Field , Username , NewField) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute("UPDATE players SET '{}' = '{}' WHERE username = '{}'" .format(Field , NewField , Username))
    conn.commit ()
def main () : 
    CreateTables ()
if __name__=='__main__' : 
    main()