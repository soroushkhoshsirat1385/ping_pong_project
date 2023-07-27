from SQL import * 
# def AddNewPlayerToDB () : 
#     pass
# def RemovePlayerFromDB () : 
#     pass
# def ChangePlayerUsername () : 
#     pass
# def Plus (a) :
#     return a+1
# def ChangePlayerPassword () : 
#     pass 
# def ChangePlayerAttributes (Field , CurrentField , NewField) :
#     #find where Field equals CurrentField and change it to NewField 
#     pass 
class player :
    def __init__(self , user_name , name , rating , last_name , password) :
        self.UserName = user_name
        self.Name = name
        self.Rating = rating 
        self.LastName = last_name
        self.Password = password
        # AddNewPlayerToDB (user_name,name,rating,last_name) 
    def RemovePlayer (self) : 
        pass 
        # RemovePlayerFromDB (self.Name , self.LastName)
    def ChangeUsername (self , new_username):
        pass 
        # ChangePlayerUsername (self.UserName , new_username) 
    def ChangePlayerPassword (self , new_password) : 
        pass 
        # ChangePlayerPassword (self.Password , new_password)
def CMD () : 
    main()
    
if __name__=='__main__' : 
    CMD()
