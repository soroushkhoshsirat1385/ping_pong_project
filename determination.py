def Service_determination (player1score : int , player2score : int , server : int , otherplayer : int) : 
    if player1score <= 10 & player2score <= 10 : 
        sum = player1score+player2score 
        if sum%2==0 :
            if sum % 4 == 0 : 
                return server
            else : 
                return otherplayer 
        else : 
            sum -= 1 
            if sum % 4 == 0 : 
                return server
            else : 
                return otherplayer 
    else : 
        sum = player1score + player2score 
        if sum %2 == 0 : 
            return server 
        else : 
            return otherplayer 