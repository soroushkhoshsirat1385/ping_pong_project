import SQL as sql 

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

def main () : 
    sql.
if __name__=='__main__' :  
    main () 
