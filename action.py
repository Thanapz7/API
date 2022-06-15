from conDB import Con 
c = Con

class Action:
    def getHW():
        data = c.getHW()
        return data
    
    def updateHW(ID, status):
        t = c.updateHW(ID, status)
        if(t == True):
            data = c.selectHW_byid(ID)
        else:
            data = {"error": True}
        return data
    
    def selectHW_byid(ID):
        data = c.selectHW_byid(ID)
        return data
    
    def insertHW(name, hw_name):
        ID = c.insertHW(name, hw_name)
        if(ID):
            data = c.selectHW_byid(ID)
        else:
            data = {"error": True}
        return data
    
    def deleteHW(ID):
        t = c.deleteHW(ID)
        if(t == True):
            data = c.getHW()
        else:
            data = {"error" : True}
        return data
    
    
            