class User :
    def __init__(self,name,userID):
        self.name =name
        self.email = name + "@gmail.com"
        self.userID = userID
    
    def getData(self):
        return {'id' : self.userID , 'name' : self.name  , 'email':self.email}


class cards :
    def __init__(self,name,cardID) :
        self.name =name
        self.cardID = cardID
        self.assigned = "UNASSIGN"
        self.assignedto = ""
        self.description = ""
    
    def Assign_card(self,emailID) :
        self.assignedto = emailID
    
    def getData(self) :
        temp = {'id' : self.cardID , 'name' : self.name  , 'assignedto' : self.assignedto , 'description' : self.description}
        return {k: v for k, v in temp.items() if v != ""  }

    
    

