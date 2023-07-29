from SQL import * 

class player :
    def __init__(self , user_name : str, name :str, rating :int , last_name :str , password :str) :
        self.UserName = user_name
        self.Name = name
        self.Rating = rating 
        self.LastName = last_name
        self.Password = password
        AddPlayer(self) 
    def RemovePlayer (self) : 
        pass     def ChangeUsername (self , new_username):
        ChangePlyaerAttributes("username" , self.UserName , new_username)
        self.UserName = new_username
        # ChangePlayerUsername (self.UserName , new_username) 
    def ChangePassword (self , new_password) : 
        ChangePlyaerAttributes("player_passwrd" , self.UserName , new_password) 
        # ChangePlayerPassword (self.Password , new_password)
def main () : 
    player1 = player("soroush1385" , "soroush" , 1300 , "pir khosh sirat" , "s13851009")
    player1.ChangePassword("s138510091")
if __name__=='__main__' :  
    main () 
