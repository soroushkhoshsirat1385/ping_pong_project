import SQL as sql 
import determination as determination
import consts as consts

class player :
    def __init__(self , user_name : str, name :str, rating :int , last_name :str , password :str) :
        self.UserName = user_name
        self.Name = name
        self.Rating = rating 
        self.LastName = last_name
        self.Password = password
        sql.AddPlayer(self) 
    def ChangeName (self , new_name) : 
        sql.ChangePlyaerAttributes(consts.DataBase.get("name" , self.UserName , new_name))
        self.Name = new_name
    def ChangeLastName (self , new_lassname) : 
        sql.ChangePlyaerAttributes(consts.DataBase.get("lastname") , self.UserName , new_lassname) 
        self.LastName=new_lassname
    def RemovePlayer (self) : 
        sql.RemovePlayer(self)
    def ChangeUsername (self , new_username):
        sql.ChangePlyaerAttributes(consts.DataBase.get("username") , self.UserName , new_username)
        self.UserName = new_username
    def ChangePassword (self , new_password) : 
        sql.ChangePlyaerAttributes(consts.DataBase.get("password") , self.UserName , new_password) 
        self.Password = new_password

class configuration : 
    def __init__ (self , rounds : int , points_per_round : int , time_outs_duration : float , time_outs_per_game : int ) : 
        self.rounds = rounds 
        self.PPR = points_per_round 
        self.TPG = time_outs_per_game 
        self.TOD = time_outs_duration 

class game : 
    def __init__(self , player1 : player , player2 : player , config : configuration ):
        self.player1 = player1  
        self.player2 = player2
        self.config = config 
    def InitGame (self) : 
        ID = sql.AddGame(self)
        determination.Determine_server ()
        loop_game (self,  ID) 

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

def loop_game (game : game , ID : int) : 
    config = sql.ReturnConfigByID (ID)
    print (config)
def main () : 
    sql.CreateTables()
    
    # player1 = player ("soroush" , "soroush" , 1000 , "khoshsirat" , "s13851009")
    # player1.RemovePlayer()
    # err = MakeConfig (1,1,1,0) 
    # if err != "ok" : 
        # print ("error while creating new config : %s" %err)
    # player2 = player ("soroush2" , "soroush" , 1000 , "khoshsirat" , "s13851009")
    # config1 = configuration(5 , 11 , 1.5 , 2)
    # sql.ReturnConfigByID("igd")
    # game1 = game(player1 , player2 , config1)
    # game1.InitGame()
    # game1.InitGame()

if __name__=='__main__' :  
    main () 
