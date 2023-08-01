import SQL as sql 
import determination as determination

def loop_game () : 
    pass
class player :
    def __init__(self , user_name : str, name :str, rating :int , last_name :str , password :str) :
        self.UserName = user_name
        self.Name = name
        self.Rating = rating 
        self.LastName = last_name
        self.Password = password
        sql.AddPlayer(self) 
    def RemovePlayer (self) : 
        pass 
    def ChangeUsername (self , new_username):
        sql.ChangePlyaerAttributes("username" , self.UserName , new_username)
        self.UserName = new_username
    def ChangePassword (self , new_password) : 
        sql.ChangePlyaerAttributes("player_passwrd" , self.UserName , new_password) 
class configuration : 
    def __init__ (self , rounds : int , points_per_round : int , time_outs_duration : float , time_outs_per_game : int ) : 
        self.rounds = rounds 
        self.PPR = points_per_round 
        self.TPG = time_outs_per_game 
        self.TOD = time_outs_duration 
class game : 
    def __init__(self , player1 : player , player2 : player , config : configuration ) -> None:
        self.player1 = player1  
        self.player2 = player2
        self.config = config 
    def InitGame (self) : 
        sql.AddGame(self)
        determination.Determine_server ()
        loop_game () 

def main () : 
    sql.CreateTables()
    # player1 = player ("soroush" , "soroush" , 1000 , "khoshsirat" , "s13851009")
    # player2 = player ("soroush2" , "soroush" , 1000 , "khoshsirat" , "s13851009")
    # config1 = configuration(5 , 11 , 1.5 , 2)
    # game1 = game(player1 , player2 , config1)
    # game1.InitGame()
if __name__=='__main__' :  
    main () 
