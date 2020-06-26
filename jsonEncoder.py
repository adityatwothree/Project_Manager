import json
from json import JSONEncoder

class BoardEncoder(JSONEncoder):
        def default(self, o):
            temp2 = []
            temp4 =[]
            temp3 = []
            for x in o.lists_members.values() :
                temp2.append(x.getData())
                for y in x.cards_members.values():
                    temp4.append(y.getData())

            for x in o.members.values() :
                temp3.append(x.getData())
            temp = {'id':o.id,'name':o.name,'privacy':o.privacy,'lists':temp2,'cards' : temp4,'users': temp3}
            return {k: v for k, v in temp.items() if v != [] and v != {}  }


class listEncoder(JSONEncoder):
        def default(self, o):
            temp2=[]
            for x in o.cards_members.values() :
                temp2.append(x.getData())

            temp = {'id' : o.listID , 'name' : o.name , 'cards' : temp2}
            return {k:v for k, v in temp.items() if len(v) != 0  }
                
class cardEncoder(JSONEncoder):
        def default(self, o):
            temp = {'id' : o.cardID , 'name' : o.name  , 'assignedto' : o.assignedto , 'description' : o.description}
            return {k: v for k, v in temp.items() if len(v) != 0  }
        