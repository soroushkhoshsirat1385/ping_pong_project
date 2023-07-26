def AddNewPlayerToDB () : 
    pass
def RemovePlayerFromDB () : 
    pass
def ChangePlayerUsername () : 
    pass
class player :
    def __init__(self , user_name , name , rating , last_name) :
        self.UserName = user_name
        self.Name = name
        self.Rating = rating 
        self.LastName = last_name
        AddNewPlayerToDB (user_name,name,rating,last_name) 
    def RemovePlayer (self) : 
        RemovePlayerFromDB (self.Name , self.LastName)
    def ChangeUsername (self , new_username):
        ChangePlayerUsername (self.UserName , new_username) 
