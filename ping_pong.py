import sqlite3 
from sqlite3 import Error
import uuid 
import datetime
import time
from dataclasses import dataclass
from tkinter import *
#constes
playerconsts = {
    "password" : "player_password" , 
    "username" : "username" ,
    "lastnaem" : "player_lastname" , 
    "name" : "player_name" , 
    "rating" : "rating" 
}
#data classes
@dataclass
class playerdataclass :
    player_name : str
    username : str
    lastname : str 
    password : str
    rating : int 
@dataclass
class gamedataclass : 
    player1username : str 
    player2username : str
    game_start_time : str 
    score :str 
    game_ID : int 
@dataclass
class configdataclass :
    game_id : str 
    rounds : int
    PPR : int 
    TPG : int 
    TOD : int 
#class section pt 1 
class configuration : 
    def __init__ (self , rounds : int , points_per_round : int , time_outs_duration : float , time_outs_per_game : int ) : 
        self.rounds = rounds 
        self.PPR = points_per_round 
        self.TPG = time_outs_per_game 
        self.TOD = time_outs_duration 
class player : 
    def __init__(self , user_name : str, name :str, rating :int , last_name :str , password :str) :
        self.UserName = user_name
        self.Name = name
        self.Rating = rating 
        self.LastName = last_name
        self.Password = password
class game : 
    def __init__(self , player1 : player , player2 : player , config : configuration ):
        self.player1 = player1  
        self.player2 = player2
        self.config = config 
        self.player1score = 0 
        self.player2score = 0 
        self.server = 0 
        self.otherPlayer = 0 
        self.currentGame = 0 
        self.player1games = 0 
        self.player2games = 0 
        self.player1timeouts = 0
        self.player2timeouts = 0
    def InitGame (self) : 
        ID = AddGame(self)
        loop_game (self,  ID) 
#sqlite section
try:
    conn = sqlite3.connect("ping_pong.db")
except Error as e:
    print(e)  
def ReturnConfigByID (ID) : 
    try : 
       cur=conn.cursor () 
    except Error as e :
        print (e)
    configs: list[configdataclass] = cur.execute("SELECT * FROM configs WHERE game_id = '{}'".format(ID)).fetchall()
    for row in configs:
        config1 : configdataclass = configdataclass(*row)
        print(config1.game_id)
    return configs
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
    cur.execute("CREATE TABLE IF NOT EXISTS logs (game_id TEXT , log_msg TEXT , log_time TEXT)")
    conn.commit()
def ChackNotDuplicateUsernames (player : player) : 
    try : 
        cur = conn.cursor()
    except Error as e : 
        print (e)
    players : list[playerdataclass] = cur.execute("SELECT * FROM players WHERE username = '{}'".format(player.UserName)).fetchall()
    if len(players) == 0: 
        return True
    else :
        return False
def AddPlayer (player : player) : 
    try : 
       cur=conn.cursor () 
    except Error as e :
        print (e)
    if ChackNotDuplicateUsernames (player): 
        cur.execute("""INSERT INTO players VALUES ('{}' , '{}' , '{}' , '{}' , {})""".format(player.Name , player.UserName , player.LastName , player.Password , player.Rating))
        conn.commit ()
        print ("added a new player")
    else : 
        print("you can not add players with same username")
def RemovePlayer(player : player ) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
        print (e)
    cur.execute("""DELETE FROM players WHERE username='{}'""".format(player.UserName))
    conn.commit()
def AddConfig (game: game , ID : int) : 
    try : 
        cur = conn.cursor() 
    except Error as a : 
        print(a) 
    cur.execute("""INSERT INTO configs VALUES ('{}' , {} , {} , {} , {})""".format(ID , game.config.rounds , game.config.PPR , game.config.TPG , game.config.TOD))
    conn.commit()
def AddGame (game: game) : 
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
def ChangePlyaerAttributes (Field , UserName , NewField) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
            print (e)
    cur.execute("UPDATE players SET '{}' = '{}' WHERE UserName = '{}'" .format(Field , NewField , UserName))
    conn.commit ()
def log (game_ID , msg : str) : 
    try : 
        cur=conn.cursor () 
    except Error as e :
            print (e)
    cur.execute("INSERT INTO logs VALUES ('{}' , '{}' , '{}')".format(game_ID , msg , datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
#class section pt2  
class player :
    def __init__(self , user_name : str, name :str, rating :int , last_name :str , password :str) :
        self.UserName = user_name
        self.Name = name
        self.Rating = rating 
        self.LastName = last_name
        self.Password = password
        AddPlayer(self)
    def ChangeName (self , new_name) : 
        ChangePlyaerAttributes(playerconsts.get("name" , self.UserName , new_name))
        self.Name = new_name
    def ChangeLastName (self , new_lassname) : 
        ChangePlyaerAttributes(playerconsts.get("lastname") , self.UserName , new_lassname) 
        self.LastName=new_lassname
    def RemovePlayer (self) : 
        RemovePlayer(self)
    def ChangeUsername (self , new_username):
        ChangePlyaerAttributes(playerconsts.get("username") , self.UserName , new_username)
        self.UserName = new_username
    def ChangePassword (self , new_password) : 
        ChangePlyaerAttributes(playerconsts.get("password") , self.UserName , new_password) 
        self.Password = new_password
#validation section 
def Server_determination_validate (input) : 
    pass
def Server_determination_validation (input) : 
    pass
#determination section
def Service_determination (game:game) : 
    if game.player1score <= 10 & game.player2score <= 10 : 
        sum = game.player1score+game.player2score 
        if sum%2==0 :
            if sum % 4 == 0 : 
                return game.server
            else : 
                return game.otherPlayer 
        else : 
            sum -= 1 
            if sum % 4 == 0 : 
                return game.server
            else : 
                return game.otherPlayer 
    else : 
        sum = game.player1score + game.player2score 
        if sum %2 == 0 : 
            return game.server 
        else : 
            return game.otherPlayer 
def Server_determination (game :game , ID) : 
    print ("determine the server please")
    print ("""who is the server : \nplayer 1 : '{}'\nplayer 2 : '{}'""".format(game.player1.UserName , game.player2.UserName))
    userinput = int(input())
    Server_determination_validation (userinput)
    if userinput == 1 : 
        game.server = game.player1 
        game.otherPlayer = game.player2
        log (ID , "player 1 is the server of the game")
    else : 
        game.server = game.player2 
        game.otherPlayer = game.player1
        log (ID , "player 2 is the server of the game")
def CheckIfGameNotEnded (player1score , player2score) : 
    if player1score < 11 and player2score < 11 : 
        return False 
    elif abs(player2score-player1score) >= 2 :
        return True
    else : 
        return False
def ChackIfMatchNotEnded (game : game , config : configuration) : 
    games = int (config[0][1]/2) + 1 
    if game.player1games == games or game.player2games == games : 
        return True
    else :
        return False
#main program 
def MakeConfig (rounds : int , PPR : int , TOD : int , TPG : int) :
    if rounds%2 == 0 :
        return ValueError("rounds must be a odd number")
    if PPR%2==0 : 
        return ValueError("Points per round must be odd")
    if TPG > 0 & TOD < 0.5 : 
        return ValueError("time out duration cant be less than half a minute")
    if TPG < 0 : 
        return ValueError("time out per game must be posetive or 0")
    configuration(rounds,PPR,TOD,TPG)
    return "ok"
def loop_game (game1 : game , ID : int) :
    log (ID , "init match")
    config = ReturnConfigByID (ID)
    game1.player1timeouts = config[0][3]
    game1.player2timeouts = config[0][3]
    # print (config) # ID , rounds , points per round , time out per game , time out duration
    Server_determination(game1 , ID)
    for i in range (config[0][1]) :
        log (ID , "init game {}".format(i+1))
        while 1 :   
            print ("game {}".format(i+1))
            print ("player 1 points : {} \nplayer 2 points : {}".format(game1.player1score , game1.player2score)) 
            print ("""who won the point \nplayer 1 : '{}'\nplayer 2 : '{}'""".format(game1.player1.UserName , game1.player2.UserName))
            userinput = input()
            try : 
                userinput = int(userinput)
            except : 
                print ("please enter the right amount")
            # validation and try/expect
            if userinput == 1 :
                game1.player1score += 1 
                log (ID , "player 1 won a point , points : {} , {}".format(game1.player1score , game1.player2score))
            if userinput == 2 : 
                game1.player2score += 1 
                log (ID , "player 2 won a point , points : {} , {}".format(game1.player1score , game1.player2score))
            if userinput == 3 : 
                if config[0][3] != 0:
                    print ("who wants the time out : \nplayer1 : '{}' \nplayer2 : '{}'".format(game1.player1.UserName , game1.player2.UserName))
                    userinput1 = int(input())
                    if userinput1 == 1 :
                        if game1.player1timeouts != 0 :  
                            game1.player1timeouts -= 1
                            log (ID , "player 1 got a time out")
                            time.sleep(config[0][4] * 60)
                        else : 
                            log(ID , "player 1 requested a time out but rejected because he/she ran out of time outs")
                            print ("player 1 has no time outs left") 
                    if userinput1 == 2 :
                        if game1.player2timeouts != 0 :  
                            game1.player2timeouts -= 1
                            log (ID , "player 1 got a time out")
                            time.sleep(config[0][4])
                        else : 
                            log(ID , "player 2 requested a time out but rejected because he/she ran out of time outs")
                            print ("player 2 has no time outs left") 
                else : 
                    log (ID , "players requested a time out but rejected be cause of the settings")
                    print("time outs are not allowed in the game")
            if CheckIfGameNotEnded (game1.player1score , game1.player2score) : 
                break 
        if game1.player1score > game1.player2score : 
            game1.player1games += 1 
            log (ID , "player 1 won a game , games : {} , {}".format(game1.player1games , game1.player2games))
            print ("player 1 won the game")
        else : 
            game1.player2games += 1 
            log (ID , "player 2 won a game , games : {} , {}".format(game1.player1games , game1.player2games))
            print ("player 2 won the game")
        game1.player1score = 0 
        game1.player2score = 0 
        print ("games : \nplayer1 : {}\nplayer2 : {}".format(game1.player1games , game1.player2games))
        if ChackIfMatchNotEnded (game1 , config) : 
            if game1.player2games < game1.player1games : 
                log (ID , "player 1 won the match")
                print ("player 1 won the match")
            else : 
                log (ID , "player 2 won the match")
                print ("player 2 won the match")
            break 
        for i in range (60) : 
            print ("time out between games : ",i+1 , end="\r") 
            time.sleep(1)
    root.mainloop() # the window is now displayed
def main () : 
    CreateTables()
    
    player1 = player ("soroush" , "soroush" , 1000 , "khoshsirat" , "s13851009")
    player1.RemovePlayer()
    err = MakeConfig (1,1,1,0) 
    if err != "ok" : 
        print ("error while creating new config : %s" %err)
    player2 = player ("soroush2" , "soroush" , 1000 , "khoshsirat" , "s13851009")
    config1 = configuration(5 , 11 , 0.5 , 2)
    # sql.ReturnConfigByID("igd")
    game1 = game(player1 , player2 , config1)
    # game1.InitGame()
    game1.InitGame()
if __name__=='__main__' :  
    main () 
